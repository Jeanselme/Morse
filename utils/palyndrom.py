import utils.morse as morse

def standard_palyndrome(word):
    """
        Returns if the word is a palyndrom

        Arguments:
            word {str} -- Word in any latin language

        Returns:
            bool -- True if palyndrom
    """
    word = word.replace(" ", "")
    return word == word[::-1]

def morse_palyndrome(word):
    """
        Returns if the word is a palyndrom in morse
    
        Arguments:
            word {str} -- Word in any latin language

        Returns:
            bool -- True if palyndrom
    """
    morse_word = morse.encrypt(word)
    return standard_palyndrome(morse_word)