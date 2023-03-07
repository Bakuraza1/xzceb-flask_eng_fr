"""Module to do unittest of translator.py module"""
import unittest
from ..translator import french_to_english, english_to_french

class TestTranslate(unittest.TestCase):
    """Class to make unittest"""
    def test_fe(self):
        """Test frenchToEnglish function"""
        self.assertEqual(french_to_english(""), "No text as input")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_ef(self):
        """Test englishToFrench function"""
        self.assertEqual(english_to_french(""), "No text as input")
        self.assertEqual(english_to_french("Hello"), "Bonjour")


if __name__ == "__main__":
    unittest.main()
