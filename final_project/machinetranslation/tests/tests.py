import unittest
from translator import Translator

class TestTranslator(unittest.TestCase):
    translator = Translator()

    def testEnglishToFrench(self):
        self.assertEqual( self.translator.english_to_french(''), '' )
        self.assertEqual( self.translator.english_to_french('Hello'), 'Bonjour' )

    def testFrenchToEnglish(self):
        self.assertEqual( self.translator.french_to_english(''), '' )
        self.assertEqual( self.translator.french_to_english('Bonjour'), 'Hello' )

unittest.main()

