import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')

    def test_f2e(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')

if __name__ == '__main__':
    unittest.main()