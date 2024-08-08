import random
import wonderwords
from wonderwords import RandomWord
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
| | | | (| | | | | (| | | | | | | (_| | | | |
|| ||\,|| ||\, || || ||\,|| |_|
                    __/ |                      
                   |_/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
rw=RandomWord()
num_words=10
randomWord=[rw.word() for word in range(num_words)]
choosen_word=random.choice(randomWord)

lives=6
display=[]
for blanks in range(len(choosen_word)):
    display+='_'

guessed_letters=set()
print(stages[lives])
while ''.join(display) != choosen_word:
    guess=input("Guess a letter: ").lower()

    if len(guess)!=1 or not guess.isalpha():
        print("Please enter single alphabetic character!")
        continue
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue
    guessed_letters.add(guess)
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if guess==letter:
            display[position]=letter           
    if guess not in choosen_word:
        lives-=1
        print(stages[lives])
        if lives==0:
            print(f"you lose! the word was {choosen_word}")
            exit()
    print (''.join(display))
if ''.join(display)==choosen_word:
    print("You Won!")