# /src/decrypt_text.py-1-A+
# Decrypts the encrypted emoji text back into the original text.

import json
import logging
import re

def load_cipher(file_path="cipher.json"):
    """
    Load the emoji cipher mappings from a JSON file.
    
    Parameters:
    - file_path (str): The path to the JSON file containing the cipher mappings.
    
    Returns:
    - dict: A dictionary with characters as keys and lists of emojis as values.
    """
    logging.info(f"Loading cipher from {file_path}")
    try:
        logging.info(f"Loading cipher from {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            cipher = json.load(file)
            logging.info("Cipher loaded successfully")
            return cipher
    except FileNotFoundError:
        logging.error("Cipher file not found.")
        return {}
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in cipher file.")
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
    logging.info("Starting decryption")
    cipher = load_cipher(cipher_path)
    # Inverting the cipher for decryption: mapping each emoji to its corresponding character
    emoji_to_char = {v: k for k, vs in cipher.items() for v in vs}

    # Prepare a regex pattern to match any of the emojis in the text
    pattern = '|'.join(re.escape(emoji) for emoji in emoji_to_char.keys())
    # Use the pattern to find and replace each emoji in the encrypted text
    decrypted_text = re.sub(pattern, lambda match: emoji_to_char[match.group(0)], encrypted_text)

    logging.info("Decryption completed")
    return decrypted_text
