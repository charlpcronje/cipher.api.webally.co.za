import json

# Define the path to the cipher file
cipher_path = "../cipher.json"

# This function will load the cipher from the specified JSON file
def load_cipher(file_path):
    """
    Load the cipher from the specified JSON file.
    
    Parameters:
    - file_path (str): Path to the JSON file containing the cipher.
    
    Returns:
    - dict: A dictionary with the cipher data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# This function will check for duplicate emojis and list them
def find_duplicate_emojis(cipher):
    """
    Identifies duplicate emojis in the cipher mapping.
    
    Parameters:
    - cipher (dict): The cipher mapping.
    
    Returns:
    - set: A set of duplicate emojis.
    """
    # Flatten the cipher into a list of all emojis
    all_emojis = [emoji for sublist in cipher.values() for emoji in sublist]
    
    # Find duplicates by checking if the count is greater than 1
    duplicates = set([emoji for emoji in all_emojis if all_emojis.count(emoji) > 1])
    
    return duplicates

# Load the cipher
cipher = load_cipher(cipher_path)

# Check for duplicates in the cipher
duplicates = find_duplicate_emojis(cipher)

# Print out the duplicates
print("Duplicate emojis:", duplicates)
