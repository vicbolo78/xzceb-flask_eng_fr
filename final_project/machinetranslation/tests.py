"""Testing"""
import unittest
from translator import english_to_french, french_to_english
class TestEnglishToFrench(unittest.TestCase):
    """english to french translation"""
    def test_english_to_french(self):
        """english to french translation"""
        self.assertNotEqual(english_to_french('none'),'')
        self.assertNotEqual(english_to_french(0),0)
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        
class TestFrenchToEnglish(unittest.TestCase):
    """french to english translation"""
    def test_french_to_english(self):
        """english to french translation"""
        self.assertNotEqual(french_to_english('none'),'')
        self.assertNotEqual(french_to_english(0),0)
        self.assertEqual(french_to_english('Bonjour'),'Hello')
       
if __name__=='__main__':
    unittest.main()
