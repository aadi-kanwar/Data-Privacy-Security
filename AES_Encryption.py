import Crypto
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
def aes_encrypt_decrypt():
  # Step 1: Define plaintext and generate a key
  plaintext = b"This is a secret message to be encrypted." # Message to encrypt
  key = get_random_bytes(16) # AES-128 requires a 16-byte key  
  # Step 2: Pad plaintext to match AES block size (16 bytes)
  padded_plaintext = pad(plaintext, AES.block_size)
  
  # Step 3: Generate a random Initialization Vector (IV)
  iv = get_random_bytes(AES.block_size)

  # Step 4: Encrypt the plaintext using AES-CBC mode
  cipher = AES.new(key, AES.MODE_CBC, iv)
  ciphertext = cipher.encrypt(padded_plaintext)
  # Display the encrypted data
  print("Original Plaintext:", plaintext.decode())
  print("Padded Plaintext:", padded_plaintext)
  print("Ciphertext (Hex):", ciphertext.hex())
  print("-" * 50)
  # Step 5: Decrypt the ciphertext
  cipher_decrypt = AES.new(key, AES.MODE_CBC, iv) # Use the same key and IV
  decrypted_data = cipher_decrypt.decrypt(ciphertext)
  # Unpad the decrypted data
  decrypted_plaintext = unpad(decrypted_data, AES.block_size)
  # Display the decrypted data
  print("Decrypted Plaintext:", decrypted_plaintext.decode())
  # Run the encryption and decryption process
  

if __name__ == "__main__":
  aes_encrypt_decrypt()