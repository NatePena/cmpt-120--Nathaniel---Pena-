def join_strings(strings):
    return ''.join(strings)


def mad_libs(name: str, noun: str, event: str) -> str:
    return f"{name} is too cool for {noun} class. Instead she/he will be attending the {event}"


def caesar_cipher(text, shift):
    """
    Encrypts or decrypts the given text using the Caesar cipher algorithm.

    :param text: The text to be encrypted/decrypted.
    :type text: str

    :param shift: The amount of shift to apply to the text. Positive shift value is for encryption and negative shift value is for decryption.
    :type shift: int

    :return: The encrypted/decrypted text.
    :rtype: str
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ''

    for char in text:
        if char.isalpha():
            # Find the index of the character in the alphabet
            idx = alphabet.index(char.lower())

            # Calculate the shifted index
            shifted_idx = (idx + shift) % 26

            # Get the new character from the alphabet
            new_char = alphabet[shifted_idx]

            # Add the character to the cipher text
            cipher_text += new_char if char.islower() else new_char.upper()
        else:
            # Add non-alphabetic characters as-is
            cipher_text += char

    return cipher_text
