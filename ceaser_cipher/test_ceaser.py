import unittest

from caesar import encryption_caesar, decryption_caesar


class CaesarCipherTests(unittest.TestCase):
    def test_encryption_caesar(self):
        # Test encryption for English text with positive shift
        self.assertEqual(encryption_caesar("Hello, World!", 3), "Khoor, Zruog!")
        # Test encryption for Russian text with positive shift
        self.assertEqual(encryption_caesar("Привет, Мир!", 5), "Фхнжйч, Снх!")
        # Test encryption for English text with zero shift
        self.assertEqual(encryption_caesar("Hello, World!", 0), "Hello, World!")
        # Test encryption for Russian text with zero shift
        self.assertEqual(encryption_caesar("Привет, Мир!", 0), "Привет, Мир!")
        # Test encryption for both Russian and English text with 0 shift
        self.assertEqual(encryption_caesar("Abcd Абвг", 0), "Abcd Абвг")
        # Test encryption for both Russian and English text with positive shift
        self.assertEqual(encryption_caesar("Abcd Абвг", 5), "Fghi Еёжз")
        # Test encryption for both Russian and English text with negative shift
        self.assertEqual(encryption_caesar("Abcd Абвг", -5), "Vwxy Ыьэю")
        # Test encryption for empty text
        self.assertEqual(encryption_caesar("", 3), "")
        # Test encryption for text without alphabetic characters
        self.assertEqual(encryption_caesar("12345!@#$%", 3), "12345!@#$%")

    def test_decryption_caesar(self):
        # Test decryption for English text with positive shift
        self.assertEqual(decryption_caesar("Khoor, Zruog!", 3), "Hello, World!")
        # Test decryption for Russian text with positive shift
        self.assertEqual(decryption_caesar("Фхнжйч, Снх!", 5), "Привет, Мир!")
        # Test decryption for English text with zero shift
        self.assertEqual(decryption_caesar("Hello, World!", 0), "Hello, World!")
        # Test decryption for Russian text with zero shift
        self.assertEqual(decryption_caesar("Привет, Мир!", 0), "Привет, Мир!")
        # Test decryption for both Russian and English text with 0 shift
        self.assertEqual(decryption_caesar("Abcd Абвг", 0), "Abcd Абвг")
        # Test decryption for both Russian and English text with positive shift
        self.assertEqual(decryption_caesar("Fghi Еёжз", 5), "Abcd Абвг")
        # Test decryption for both Russian and English text with negative shift
        self.assertEqual(decryption_caesar("Vwxy Ыьэю", -5), "Abcd Абвг")
        # Test decryption for empty text
        self.assertEqual(decryption_caesar("", 3), "")
        # Test decryption for text without alphabetic characters
        self.assertEqual(decryption_caesar("12345!@#$%", 3), "12345!@#$%")


if __name__ == "__main__":
    unittest.main()
