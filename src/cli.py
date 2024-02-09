# /src/cli.py-1-A+
# CLI tool to encrypt and decrypt text via the Flask API
# /src/cli.py-2-A+ | Update to include help message
import requests
import sys

API_BASE_URL = "http://localhost:5100"

def print_help():
    """
    Prints help information for using the CLI tool.
    """
    help_text = """
    Usage:
        python cli.py encrypt <text> - Encrypts text using the API.
        python cli.py decrypt <encrypted_text> - Decrypts text using the API.
        python cli.py -help - Shows this help message.
    """
    print(help_text)

def encrypt_text(text):
    response = requests.post(f"{API_BASE_URL}/encrypt", json={"text": text})
    print("Status Code:", response.status_code)  # Debugging line
    print("Response Body:", response.text)  # Debugging line
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
    if len(sys.argv) < 2 or sys.argv[1] in ['-help', '--help']:
        print_help()
    elif len(sys.argv) < 3:
        print("Insufficient arguments provided.")
        print_help()
    else:
        action = sys.argv[1]
        text = " ".join(sys.argv[2:])
        
        if action == "encrypt":
            print("Encrypted text:", encrypt_text(text))
        elif action == "decrypt":
            print("Decrypted text:", decrypt_text(text))
        else:
            print("Invalid action specified.")
            print_help()
