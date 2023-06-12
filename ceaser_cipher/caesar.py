from string import ascii_lowercase
from string import ascii_uppercase

ascii_alphabet_length = len(ascii_lowercase)
rus_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
rus_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
rus_alphabet_length = len(rus_lowercase)

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
            if char.isupper() and char in available_character_set:
                offset = rus_uppercase if char in rus_uppercase else ascii_uppercase
            elif char.islower() and char in available_character_set:
                offset = rus_lowercase if char in rus_lowercase else ascii_lowercase

            index = offset.index(char)
            shifted_index = (index + shift) % len(offset)
            encrypted_char = offset[shifted_index]
            encrypted_text += encrypted_char
        else:
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
    # Дешифровка эквивалентна шифрованию с отрицательным смещением
    return encryption_caesar(text, -shift)


if __name__ == "__main__":
    print(encryption_caesar("Abcd Абвг", -5))
