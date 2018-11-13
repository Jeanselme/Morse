import utils.morse as morse
import unittest

class Morse(unittest.TestCase):
    
    def test_encrypt_decrypt(self):
        message = 'Hello How Are You Today ?'
        morse_message = morse.encrypt(message)
        message_translated = morse.decrypt(morse_message)

        self.assertEqual(message.upper(), message_translated)

if __name__ == '__main__':
    unittest.main()