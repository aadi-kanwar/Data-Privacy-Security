# 20.01.2025
# Caesar Cipher for Confidentiality

# Function to encrypt plaintext using Caesar Cipher
def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97  # Handle uppercase and lowercase letters
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters (like spaces or punctuation) are not changed
    return encrypted_text

# Function to decrypt Caesar Cipher
def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)  # Decrypt by shifting in the opposite direction

# Example usage
# plain_text = "Hello, What an amazing day!"
plain_text = input("Enter the plain text: ")
shift = 3  # Number of positions to shift for encryption

# Encrypt the plain text
encrypted_text = caesar_cipher_encrypt(plain_text, shift)
# Decrypt the encrypted text
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

# Output
print("Plain Text: ", plain_text)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)
