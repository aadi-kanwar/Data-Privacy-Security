import hashlib

def hash_with_md5(input_string):
  md5_hash = hashlib.md5()
  md5_hash.update(input_string.encode('utf-8'))
  return md5_hash.hexdigest()

if __name__ == "__main__":
  # Example usage
  data = input("Enter the string to hash using MD5: ")
  hashed_value = hash_with_md5(data)
  print(f"MD5 Hash: {hashed_value}")