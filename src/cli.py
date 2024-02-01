# /src/cli.py-1-A+
# CLI tool to encrypt and decrypt text via the Flask API

import requests
import sys

API_BASE_URL = "http://localhost:5000"

def encrypt_text(text):
    response = requests.post(f"{API_BASE_URL}/encrypt", json={"text": text})
    if response.status_code == 200:
        return response.json().get("encrypted_text", "")
    else:
        return "Error encrypting text."

def decrypt_text(encrypted_text):
    response = requests.post(f"{API_BASE_URL}/decrypt", json={"encrypted_text": encrypted_text})
    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        return "Error decrypting text."

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python cli.py <encrypt|decrypt> <text>")
    else:
        action = sys.argv[1]
        text = " ".join(sys.argv[2:])
        
        if action == "encrypt":
            print("Encrypted text:", encrypt_text(text))
        elif action == "decrypt":
            print("Decrypted text:", decrypt_text(text))
        else:
            print("Invalid action. Use 'encrypt' or 'decrypt'.")
