import unittest
import os, sys

sys.path.append(os.path.abspath(".."))

from machinetranslation.translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_english_to_french_null(self):
        self.assertEqual(english_to_french(None), "")

    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_english_to_french_hello_not_equal(self):
        self.assertNotEqual(english_to_french("Hello"), "Holla")

    def test_french_to_english_null(self):
        self.assertEqual(french_to_english(None), "")

    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_french_to_english_bonjour_not_equal(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Holla")

unittest.main()