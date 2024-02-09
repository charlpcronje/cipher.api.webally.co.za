# /src/encrypt_text.py-1-A+
# Encrypts the input text using the emoji cipher, where each character is replaced by a random emoji.
# Adds logging of each encryption request in a markdown format

import json
import random
import logging
from datetime import datetime
import os

def load_cipher(file_path="cipher.json"):
    """
    Load the emoji cipher mappings from a JSON file.
    
    Parameters:
    - file_path (str): The path to the JSON file containing the cipher mappings.
    
    Returns:
    - dict: A dictionary with characters as keys and lists of emojis as values.
    """
    try:
        logging.info(f"Loading cipher from {file_path}")
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
    logging.info(f"Starting encryption for text: {input_text}")
    cipher = load_cipher(cipher_path)
    encrypted_text = ""
    for char in input_text:
        if char in cipher:
            encrypted_text += random.choice(cipher[char])
        else:
            encrypted_text += char

    # Log the encryption request
    log_encryption_request(input_text, encrypted_text)

    return encrypted_text


def log_encryption_request(input_text, encrypted_text):
    """
    Logs each encryption request in a markdown file named encryptLog-{year}-{month}.md
    
    Parameters:
    - input_text (str): The original text to be encrypted.
    - encrypted_text (str): The resultant encrypted text with emojis.
    """
    now = datetime.now()
    log_file_name = f"./log/encryptLog-{now.year}-{now.month}.md"
    log_entry = f"### Encryption Request at [{now}]\n" \
                f"**Text to encrypt:** {input_text}\n" \
                f"**Emoji Output:** {encrypted_text}\n\n"
    
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file_name), exist_ok=True)
    
    # Append the log entry to the file
    with open(log_file_name, 'a', encoding='utf-8') as log_file:
        log_file.write(log_entry)
