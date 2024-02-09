import json

def load_cipher(file_path):
    """Load the emoji cipher mappings from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def remove_duplicate_emojis(cipher):
    """Removes duplicate emojis from the cipher and returns a new cipher without duplicates."""
    unique_emojis = set()
    new_cipher = {}
    for char, emojis in cipher.items():
        new_emojis = []
        for emoji in emojis:
            if emoji not in unique_emojis:
                unique_emojis.add(emoji)
                new_emojis.append(emoji)
        if new_emojis:
            new_cipher[char] = new_emojis
    return new_cipher

def save_cipher(cipher, file_path):
    """Saves the updated cipher to a new JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(cipher, file, ensure_ascii=False, indent=4)

cipher_path = "../cipher.json"
new_cipher_path = "../cipher_updated.json"

# Load the original cipher
cipher = load_cipher(cipher_path)

# Remove duplicates and get the updated cipher
updated_cipher = remove_duplicate_emojis(cipher)

# Save the updated cipher to a new file
save_cipher(updated_cipher, new_cipher_path)

print("Updated cipher saved to:", new_cipher_path)
