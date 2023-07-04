from machinetranslation.translator import english_to_french, french_to_english
import unittest

class Testtranslator(unittest.TestCase):
    def Test_english_to_french(self):
        self.assertEqual( english_to_french('Hello') , 'Bonjour')
    def Test_french_to_english(self):
        self.assertEqual( french_to_english('Bonjour') , 'hello')
        
if __name__ == "__main__":
    unittest.main()