# Concept & code taught : 09.01.2025
# # The code below is an experiment on my own to demonstrate the working of hashing.
import hashlib

def hash_string(input_string):
  sha_signature = hashlib.sha256(input_string.encode()).hexdigest()
  return sha_signature

input_string = "Hello, World!"
hash_value = hash_string(input_string)
print(f"Original string: {input_string}")
print(f"Hash value: {hash_value}")

# Demonstrate the effect of a small change in the input string
input_string_changed = "Hello, world!"
hash_value_changed = hash_string(input_string_changed)
print(f"\nChanged string: {input_string_changed}")
print(f"Hash value after change: {hash_value_changed}")