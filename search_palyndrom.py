import os
import urllib.request
from utils.palyndrom import morse_palyndrome, standard_palyndrome

# Download dictionary
path = os.path.join('dictionary', 'words_alpha.txt')
if not os.path.isdir('dictionary'):
    os.mkdir('dictionary')
if not os.path.isfile(path):
    english_dictionary = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    urllib.request.urlretrieve(english_dictionary, path)

# Open dictionary of english words
with open(path, 'r') as dic:
    words = [word for word in dic.read().splitlines()]

# Look for any palyndrom in morse
morse_palyndrom_list = []
for word in words:
    if morse_palyndrome(word):
        morse_palyndrom_list.append(word)
print("Palyndrom in morse: {}".format(morse_palyndrom_list))

# Look for all overlappin palyndrom
full_palyndrom = []
for word in morse_palyndrom_list:
    if standard_palyndrome(word):
        full_palyndrom.append(word)
print("Palyndrom in morse and in english: {}".format(full_palyndrom))
