# /src/app.py-1-A+
# Flask application to provide an API for encrypting and decrypting text using emojis.
# /src/app.py-2-A+ | Update for .env file reading

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from encrypt_text import encrypt_text  # Reference: /src/encrypt.py-1-A+
from decrypt_text import decrypt_text  # Reference: /src/decrypt.py-1-A+
from auth_utils import verify_api_key

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.before_request
def before_request():
    api_key = request.headers.get('X-API-Key')
    if not api_key:
        abort(401, description="API Key required.")
    
    valid, user = verify_api_key(api_key)
    if not valid:
        abort(403, description="Invalid API Key.")
    
    request.user = user  # Attach user data to request contexts

cipher_path = "cipher.json"

@app.route('/encrypt', methods=['POST'])
def encrypt_api():
    """
    Encrypts text sent in the request body using the emoji cipher.
    
    Expects:
    {
        "text": "<text_to_encrypt>"
    }
    
    Returns:
    {
        "encrypted_text": "<emoji_encrypted_text>"
    }
    """
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400
    
    encrypted_text = encrypt_text(data['text'], cipher_path)
    return jsonify({"encrypted_text": encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt_api():
    """
    Decrypts emoji encrypted text sent in the request body.
    
    Expects:
    {
        "encrypted_text": "<emoji_encrypted_text>"
    }
    
    Returns:
    {
        "text": "<decrypted_text>"
    }
    """
    data = request.get_json()
    if 'encrypted_text' not in data:
        return jsonify({"error": "Missing 'encrypted_text' in request body"}), 400
    
    text = decrypt_text(data['encrypted_text'], cipher_path)
    return jsonify({"text": text})

if __name__ == '__main__':
    # Fetching host and port from .env file, with default fallbacks
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    app.run(host=host, port=port, debug=True)
