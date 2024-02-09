# /src/app.py-1-A+
# Flask application to provide an API for encrypting and decrypting text using emojis.
# /src/app.py-2-A+ | Update for .env file reading

import os
import logging
from flask import Flask, request, Response, jsonify
from dotenv import load_dotenv
from encrypt_text import encrypt_text  # Reference: /src/encrypt.py-1-A+
from decrypt_text import decrypt_text  # Reference: /src/decrypt.py-1-A+
from auth_utils import verify_api_key
from flask import abort

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/privacy-policy', methods=['GET'])
def privacy_policy():
    try:
        with open('privacy_policy.html', 'r') as file:  # Assuming the policy is saved in privacy_policy.html
            privacy_policy_html = file.read()
        # Return the HTML content
        return Response(privacy_policy_html, mimetype='text/html')
    except FileNotFoundError:
        return Response("Privacy policy not found", status=404, mimetype='text/html')

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized access."}), 401


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

@app.after_request
def set_permissions_policy(response):
    # Adjust the header by removing 'document-domain'
    response.headers["Permissions-Policy"] = "feature1=(self), feature2=(self)"
    return response

@app.before_request
def before_request():
    logging.info("Checking API Key in request")
    
    # Skip API key check for the privacy policy endpoint
    if request.path == '/privacy-policy':
        return
    
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
    logging.info("Received encryption request")
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
    logging.info("Received decryption request")
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
