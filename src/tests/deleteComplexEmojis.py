import json

def is_simple_emoji(emoji):
    """
    A heuristic to check if an emoji is 'simple'.
    This function considers an emoji simple if it's comprised of a single Unicode character.
    Note: This is a basic check and might not accurately classify all emojis.
    """
    # Attempt to count the code points; this approach is simplistic and might not work for all emojis.
    return len(emoji) == 1 or (len(emoji) == 2 and ord(emoji[0]) >= 0xD800 and ord(emoji[0]) <= 0xDBFF)

def filter_simple_emojis(cipher):
    """
    Filters out complex emojis from the cipher, keeping only simple ones.
    """
    new_cipher = {}
    for char, emojis in cipher.items():
        simple_emojis = [emoji for emoji in emojis if is_simple_emoji(emoji)]
        if simple_emojis:
            new_cipher[char] = simple_emojis
    return new_cipher

def main():
    cipher_path = "../cipher.json"  # Path to your cipher file
    new_cipher_path = "../cipher_simple.json"  # Path to save the modified cipher

    # Load the original cipher
    with open(cipher_path, 'r', encoding='utf-8') as file:
        cipher = json.load(file)

    # Filter out complex emojis
    new_cipher = filter_simple_emojis(cipher)

    # Save the modified cipher
    with open(new_cipher_path, 'w', encoding='utf-8') as file:
        json.dump(new_cipher, file, ensure_ascii=False, indent=4)

    print(f"Modified cipher saved to: {new_cipher_path}")

if __name__ == "__main__":
    main()
