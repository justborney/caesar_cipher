from string import ascii_lowercase
from string import ascii_uppercase

rus_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
rus_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# All available characters for encryption and decryption
available_character_set = (
    ascii_lowercase + ascii_uppercase + rus_lowercase + rus_uppercase
)


def encryption_caesar(text: str, shift: int) -> str:
    """
    Encrypts the input string using the Caesar cipher.

    Args:
        text (str): The original string to be encrypted.
        shift (int): The number of positions to shift the characters.

    Returns:
        str: The encrypted string.

    Example:
        >>> encryption_caesar("Hello, World!", 3)
        'Khoor, Zruog!'
    """
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            # Determine the offset alphabet based on the case
            if char.isupper() and char in available_character_set:
                offset = rus_uppercase if char in rus_uppercase else ascii_uppercase
            elif char.islower() and char in available_character_set:
                offset = rus_lowercase if char in rus_lowercase else ascii_lowercase

            # Find the index of the character in the offset alphabet
            index = offset.index(char)

            # Apply the shift to the index
            shifted_index = (index + shift) % len(offset)

            # Get the encrypted character from the offset alphabet
            encrypted_char = offset[shifted_index]

            # Append the encrypted character to the result
            encrypted_text += encrypted_char
        else:
            # If the character is not a letter or
            # letter no in available character set, append it as is
            encrypted_text += char

    return encrypted_text


def decryption_caesar(text: str, shift: int) -> str:
    """
    Decrypts the encrypted string using the Caesar cipher.

    Args:
        text (str): The encrypted string to be decrypted.
        shift (int): The number of positions used for shifting characters.

    Returns:
        str: The original string.

    Example:
        >>> decryption_caesar("Khoor, Zruog!", 3)
        'Hello, World!'
    """
    # Decryption is equivalent to encryption with a negative offset
    return encryption_caesar(text, -shift)


if __name__ == "__main__":
    # Example usage of encryption_caesar function
    print(encryption_caesar("Hello, World!", 5))  # Mjqqt, Btwqi!
