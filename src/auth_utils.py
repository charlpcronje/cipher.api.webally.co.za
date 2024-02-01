# /src/auth_utils.py-1-A+
# Utility module for authentication functions in the Flask API

import json

def load_users(file_path="users.json"):
    """
    Load users and their API keys from a JSON file.
    
    Parameters:
    - file_path (str): Path to the JSON file containing user data.
    
    Returns:
    - list: A list of user dictionaries.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading user file: {e}")
        return []

def verify_api_key(api_key):
    """
    Verify the provided API key against known users.
    
    Parameters:
    - api_key (str): The API key to verify.
    
    Returns:
    - tuple: (bool, dict) indicating whether the API key is valid, and the user data.
    """
    users = load_users()
    for user in users:
        if user["api_key"] == api_key:
            return True, user
    return False, None
