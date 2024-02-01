# /src/tests/test_app.py

import unittest
import requests
import subprocess
import json
import os

def get_first_api_key(file_path="users.json"):
    """
    Reads the users.json file and returns the first API key found.
    """
    with open(file_path, 'r') as file:
        users = json.load(file)
        if users and "api_key" in users[0]:
            return users[0]["api_key"]
        return None

class TestCipherAPI(unittest.TestCase):

    def test_encrypt_endpoint(self):
        """
        Test the /encrypt endpoint.
        """
        api_key = get_first_api_key()
        # Ensure API key is present
        self.assertIsNotNone(api_key, "API key not found in users.json")

        url = "http://localhost:5100/encrypt"
        headers = {"X-API-Key": api_key}
        data = {"text": "test"}
        response = requests.post(url, json=data, headers=headers)

        result_md = f"## Test Encrypt Endpoint\n" \
                    f"**Request:**\n" \
                    f"```python\n{json.dumps(data, indent=4)}\n```\n" \
                    f"**Response:**\n" \
                    f"```python\n{response.text}\n```\n"

        with open("test_results.md", "a") as file:
            file.write(result_md)

        self.assertEqual(response.status_code, 200)

    def test_decrypt_endpoint(self):
        """
        Test the /decrypt endpoint.
        """
        api_key = get_first_api_key()
        self.assertIsNotNone(api_key, "API key not found in users.json")

        url = "http://localhost:5100/decrypt"
        headers = {"X-API-Key": api_key}
        # Assuming '🔒📄' is the encrypted text for 'test'
        data = {"encrypted_text": "🔒📄"}
        response = requests.post(url, json=data, headers=headers)

        result_md = f"## Test Decrypt Endpoint\n" \
                    f"**Request:**\n" \
                    f"```python\n{json.dumps(data, indent=4)}\n```\n" \
                    f"**Response:**\n" \
                    f"```python\n{response.text}\n```\n"

        with open("test_results.md", "a") as file:
            file.write(result_md)

        self.assertEqual(response.status_code, 200)

    def test_cli_encrypt(self):
        """
        Test the CLI encrypt command.
        """
        command = ["python", "cli.py", "encrypt", "test"]
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.strip()

        result_md = f"## Test CLI Encrypt Command\n" \
                    f"**Command:**\n" \
                    f"```bash\n{' '.join(command)}\n```\n" \
                    f"**Output:**\n" \
                    f"```python\n{output}\n```\n"

        with open("test_results.md", "a") as file:
            file.write(result_md)

        self.assertIn("Encrypted text:", output)

    def test_cli_decrypt(self):
        """
        Test the CLI decrypt command.
        """
        # Assuming '🔒📄' is the encrypted text for 'test'
        command = ["python", "cli.py", "decrypt", "🔒📄"]
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.strip()

        result_md = f"## Test CLI Decrypt Command\n" \
                    f"**Command:**\n" \
                    f"```bash\n{' '.join(command)}\n```\n" \
                    f"**Output:**\n" \
                    f"```python\n{output}\n```\n"

        with open("test_results.md", "a") as file:
            file.write(result_md)

        self.assertIn("Decrypted text:", output)

if __name__ == '__main__':
    with open("test_results.md", "w") as file:
        file.write("# Test Results\n\n")
    unittest.main()
