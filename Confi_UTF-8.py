def char_to_utf8(char):
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    utf8_value = char.encode('utf-8')
    return utf8_value

def encrypt(utf8_value, shift):
    encrypted_text = ""
    for char in utf8_value:
        encrypted_text += chr((char + shift)%256)
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr((ord(char) - shift) % 256)
    return decrypted_text

# Convert the decrypted UTF-8 value back to character
def utf8_to_char(utf8_value):
    return utf8_value.decode('utf-8')

# Example usage
character = "अ"
utf8_value = char_to_utf8(character)
e_text = encrypt(utf8_value, 4)
print(f"The UTF-8 value of '{character}' is {utf8_value}")
print(f"The encrypted value of '{character}' is {e_text}")

# Example usage of decrypt function
d_text = decrypt(e_text, 4)
print(f"The decrypted value of '{e_text}' is {d_text}")

# Example usage of utf8_to_char function
decrypted_utf8_value = bytes([ord(c) for c in d_text])
original_character = utf8_to_char(decrypted_utf8_value)
print(f"The original character from decrypted UTF-8 value is '{original_character}'")