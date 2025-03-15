from pqcrypto.kem import kyber1024

# Generate PQC key pair
public_key, private_key = kyber1024.generate_keypair()

# Load RSA-encrypted data
with open("encrypted_database.bin", "rb") as f:
    rsa_encrypted_data = f.read()

# Encrypt the RSA-encrypted data using PQC
ciphertext, shared_secret = kyber1024.encrypt(public_key)

# Save PQC-encrypted data to a file
with open("pqc_encrypted_database.bin", "wb") as f:
    f.write(ciphertext)

# Save PQC shared secret (for decryption)
with open("pqc_shared_secret.bin", "wb") as f:
    f.write(shared_secret)

print("RSA-encrypted database further encrypted using PQC.")
