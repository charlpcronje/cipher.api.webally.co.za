# /src/encrypt_text.py-1-A+
# Encrypts the input text using the emoji cipher, where each character is replaced by a random emoji.

import json
import random

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

def encrypt_text(input_text, cipher_path="cipher.json"):
    """
    Encrypts input text using emoji cipher.
    
    Parameters:
    - input_text (str): The text to be encrypted.
    - cipher_path (str): The path to the JSON file containing the emoji cipher mappings.
    
    Returns:
    - str: The encrypted text, with characters replaced by randomly selected emojis.
    """
    cipher = load_cipher(cipher_path)
    encrypted_text = ""
    for char in input_text:
        if char in cipher:
            encrypted_text += random.choice(cipher[char])
        else:
            encrypted_text += char
    return encrypted_text
