#Python Code to Demonstrate Integrity Using SHA-256 Hashing:
import hashlib

# Function to calculate the hash of a given text (using SHA-256)
def calculate_hash(text):
    # Use SHA-256 hashing algorithm
    hash_object = hashlib.sha256(text.encode())  # Encode the string into bytes
    hash_hex = hash_object.hexdigest()  # Get the hexadecimal representation of the hash
    return hash_hex

# Function to check if the integrity of the data has been preserved
def check_integrity(original_text, received_text):
    # Calculate the hash of both the original text and the received text
    original_hash = calculate_hash(original_text)
    received_hash = calculate_hash(received_text)
    
    # If the hashes are the same, integrity is preserved
    if original_hash == received_hash:
        return True  # Integrity is intact
    else:
        return False  # Integrity has been compromised

# Example usage
original_text = "He He Ho Ho"
modified_text = "Ho Ho He He"  # Modified version

# Calculate hash for the original message
original_hash = calculate_hash(original_text)

# Check integrity of the original text and the modified text
is_integrity_preserved = check_integrity(original_text, modified_text)

# Output
print("Original Text Hash:", original_hash)
print("Modified Text Hash:", calculate_hash(modified_text))
print("Is integrity preserved?", is_integrity_preserved)
