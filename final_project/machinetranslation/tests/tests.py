import unittest
import os, sys

sys.path.append(os.path.abspath(".."))

from machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrenchTranslate(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Holla")

class TestFrenchToEnglishTranslate(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english(None), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Holla")

unittest.main()