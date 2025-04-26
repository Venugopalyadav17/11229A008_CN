from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message):
    encrypted_message = cipher.encrypt(message.encode())
    print(f"Encrypted message: {encrypted_message}")
    return encrypted_message

def decrypt_message(encrypted_message):
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    print(f"Decrypted message: {decrypted_message}")
    return decrypted_message

# Simulate the cryptography process
message = "Hello, this is a secret!"
encrypted_msg = encrypt_message(message)
decrypt_message(encrypted_msg)
