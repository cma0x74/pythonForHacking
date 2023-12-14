# create a greeting
# create your word list
# randoly choose a word from the list you´ve created
# ask the user to guess a letter
# make the program convert the user´s letter to lowercase
# check if the letter is in the word

import random
import os

user = os.environ.get('USERNAME') if os.name == 'nt' else os.environ.get('USER')
print(f'Welcome {user}, thanks for using the game')

wordList = ['fail', 'lose', 'err', 'procrastinate', 'loneliness', 'shame', 'fear']
word = random.choice(wordList)

letter = input('guess a letter: ').lower()

#dps eu termino