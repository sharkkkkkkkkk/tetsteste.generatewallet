from eth_account import Account
import secrets

# Fungsi untuk generate wallet menggunakan seed phrase
def generate_wallet_from_phrase():
    # Membuat seed phrase (12 kata)
    seed_phrase = " ".join(secrets.choice(Account._default_word_list) for _ in range(12))
    
    # Generate wallet dari seed phrase
    account = Account.from_mnemonic(seed_phrase)
    
    # Informasi wallet
    wallet_info = {
        "address": account.address,
        "private_key": account.key.hex(),
        "seed_phrase": seed_phrase
    }
    
    return wallet_info

# Menjalankan fungsi
if __name__ == "__main__":
    wallet = generate_wallet_from_phrase()
    print("Wallet Generated Successfully!")
    print(f"Address: {wallet['address']}")
    print(f"Private Key: {wallet['private_key']}")
    print(f"Seed Phrase: {wallet['seed_phrase']}")
