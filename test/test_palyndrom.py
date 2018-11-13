import utils.palyndrom as palyndrom
import unittest

class Palyndrom(unittest.TestCase):
    
    def test_standard_Palyndrom(self):
        standard = "racecar"
        self.assertTrue(palyndrom.standard_palyndrome(standard))
        self.assertFalse(palyndrom.morse_palyndrome(standard))

    def test_morse_Palyndrom(self):
        morse = "pulp"
        self.assertTrue(palyndrom.morse_palyndrome(morse))
        self.assertFalse(palyndrom.standard_palyndrome(morse))

if __name__ == '__main__':
    unittest.main()