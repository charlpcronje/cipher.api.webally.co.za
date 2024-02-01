# /src/decrypt_text.py-1-A+
# Decrypts the encrypted emoji text back into the original text.

import json

def load_cipher(file_path="cipher.json"):
    """
    Load the emoji cipher mappings from a JSON file.
    
    Parameters:
    - file_path (str): The path to the JSON file containing the cipher mappings.
    
    Returns:
    - dict: A dictionary with characters as keys and lists of emojis as values.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Cipher file not found.")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON format in cipher file.")
        return {}

def decrypt_text(encrypted_text, cipher_path="cipher.json"):
    """
    Decrypts text that was encrypted with the emoji cipher.
    
    Parameters:
    - encrypted_text (str): The text to be decrypted, consisting of emojis.
    - cipher_path (str): The path to the JSON file containing the emoji cipher mappings.
    
    Returns:
    - str: The decrypted text, with emojis replaced by their corresponding characters.
    """
    cipher = load_cipher(cipher_path)
    # Create an inverse mapping from emoji to character
    emoji_to_char = {emoji: char for char, emojis in cipher.items() for emoji in emojis}
    decrypted_text = ""
    for emoji in encrypted_text:
        decrypted_text += emoji_to_char.get(emoji, emoji)  # Default to the emoji itself if not found
    return decrypted_text
