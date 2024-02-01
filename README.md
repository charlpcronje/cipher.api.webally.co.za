✖️ Below is a comprehensive `README.md` for your Flask application, structured at an A+ level with detailed explanations for each component, usage instructions, and deployment strategies.

```markdown
# Emoji Encryption and Decryption API

## Introduction
This Flask-based API provides functionality to encrypt plain text into emojis and decrypt it back to text. It's designed for secure and efficient text transformation.

## Getting Started

### Requirements
- Python 3.8 or higher
- Flask
- Gunicorn (for production deployment)
- dotenv (for environment management)

### Installation
Clone the repository and install the required packages:
```bash
git clone [your-repo-url]
cd [your-repo-name]
pip install flask gunicorn python-dotenv
```

## Configuration

### Environment Variables
Create an `.env` file in the root directory with the following variables:
```env
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
```
These variables define the host and port settings for the Flask application.

### cipher.json File
The `cipher.json` file contains mappings for the emoji encryption. It maps characters to emojis:
```json
{
  "A": ["😀", "😁"],
  "B": ["😂", "🤣"]
}
```
`encrypt_text.py` and `decrypt_text.py` use this file for encryption and decryption operations.

### users.json and Authentication
The `users.json` file stores API keys for user authentication:
```json
[
  {
    "name": "User1",
    "email": "user1@example.com",
    "api_key": "user1_api_key"
  }
]
```
`auth_utils.py` uses this file to authenticate API requests, ensuring secure access.

## Usage

### Running the Application
To start the Flask development server:
```bash
flask run --host=0.0.0.0 --port=5000
```

### Using the CLI Tool
For encryption:
```bash
python cli.py encrypt "Your text here"
```
For decryption:
```bash
python cli.py decrypt "Your encrypted text here"
```

### API Endpoints
- **Encrypt**: `/encrypt` (POST)
- **Decrypt**: `/decrypt` (POST)

Include the API key in the request header for authentication.

## Testing
Run tests using:
```bash
python -m unittest discover -s tests
```
Test results are logged in `test_results.md`.

### Test from terminal
```bash
curl -X POST http://localhost:5100/encrypt \
     -H "X-API-Key: 1234567890abcdef" \
     -H "Content-Type: application/json" \
     -d '{"text":"Hello, World!"}'
```

## Deployment

### Deploying with WSGI
Use `wsgi.py` as the entry point with Gunicorn for production:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```
Adjust the number of workers (`-w`) as necessary.

## License
Specify your license or state that the project is unlicensed.

## Contact
For support or feedback, contact us at [charl@webally.co.za](mailto:charl@webally.co.za).
```


