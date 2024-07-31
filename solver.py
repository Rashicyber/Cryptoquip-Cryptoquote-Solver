# solver.py

import string

def decrypt(ciphertext, key):
    """
    Decrypts the given ciphertext using the provided substitution key.
    
    :param ciphertext: The encrypted message.
    :param key: A dictionary mapping each letter of the alphabet to its decrypted counterpart.
    :return: The decrypted message.
    """
    decrypted_text = []
    for char in ciphertext:
        if char.lower() in key:
            decrypted_char = key[char.lower()]
            if char.isupper():
                decrypted_text.append(decrypted_char.upper())
            else:
                decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def create_key_from_mapping(mapping):
    """
    Creates a key dictionary from a given letter mapping.
    
    :param mapping: A string where the index corresponds to the original letter
                    (a-z) and the character at that index is the cipher equivalent.
    :return: A dictionary mapping cipher letters to plaintext letters.
    """
    alphabet = string.ascii_lowercase
    key = {cipher_char: plain_char for cipher_char, plain_char in zip(mapping, alphabet)}
    return key

if __name__ == "__main__":
    # Example usage
    cipher_text = "Gsrh rh z hvxivg"
    key_mapping = "zyxwvutsrqponmlkjihgfedcba"  # Example substitution key (simple reverse alphabet)
    
    key = create_key_from_mapping(key_mapping)
    decrypted_message = decrypt(cipher_text, key)
    print(f"Decrypted message: {decrypted_message}")
