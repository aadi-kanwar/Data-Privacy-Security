# Caesar Cipher for Confidentiality and Availability
# 20.01.2025

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
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text

# Example usage
# plain_text = "Ensure Data Availability!"
plain_text = input("Enter the plain text: ")
shift = 3  # Number of positions to shift for encryption

print("Plain Text:", plain_text)
# Encrypt the plain text
encrypted_text = caesar_cipher_encrypt(plain_text, shift)
print("Encrypted Text:", encrypted_text)

# Decrypt the encrypted text (Availability: Ensuring it's accessible)
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Decrypted Text (Availability):", decrypted_text)

# Availability is demonstrated by ensuring that the encrypted data can be decrypted and is accessible when needed