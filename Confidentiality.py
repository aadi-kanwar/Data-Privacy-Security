# Concept & code taught : 09.01.2025
# Hands on : 
# Encrytion & decryption of data

mapping = {
   'a': 'i', 'b': 'j', 'c': 'k', 'd': 'l', 'e': 'm', 
   'f': 'n', 'g': 'o', 'h': 'p', 'i': 'q', 'j': 'r', 
   'k': 's', 'l': 't', 'm': 'u', 'n': 'v', 'o': 'w', 
   'p': 'x', 'q': 'y', 'r': 'z', 's': 'a', 't': 'b', 
   'u': 'c', 'v': 'd', 'w': 'e', 'x': 'f', 'y': 'g', 
   'z': 'h', ' ': ' '
}

text=input("Enter the text: ")
encrypt_text = ""
def encrypt():
   global encrypt_text
   for i in text.lower():
      if i in mapping:
         encrypt_text += mapping[i]

decrypt_text = ""
def decrypt():
   global decrypt_text
   inverse_mapping = {v: k for k, v in mapping.items()}
   for i in encrypt_text:
      if i in inverse_mapping:
         decrypt_text += inverse_mapping[i]

print("Original text: ", text)
if __name__ == "__main__":
   encrypt()
   print("Encrypted text: ", encrypt_text)
   decrypt()
   print("Decrypted text: ", decrypt_text)