import random
from asciiart import HANGMANPICS
from clear import clear_terminal

word_list = ["baboon", "camel"]
lives = 6
gameover = False
choosen_word =  random.choice(word_list)
placeholder = ""

for _ in range(len(choosen_word)):
    placeholder += "_"
hangman_len = len(HANGMANPICS)
correct_letter = []

print(f'{placeholder}\n')

while not gameover:
    print(f"lives left: {lives}\n")
    display = ""

    print(HANGMANPICS[hangman_len - (lives + 1)])
    user_letter = input("Please guess a letter:\n").lower()
    found = False
    for letter in choosen_word:
        if letter == user_letter:
            found = True
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"


    clear_terminal()
    if not found:
        lives -= 1
        if lives == 0:
            gameover = True
            
            print(HANGMANPICS[-1])
            break

    

    if "_" not in display:
        gameover = True
        break

    print(f"{display}\n")


if len(correct_letter) == len(choosen_word):
    print(f"You Won!!!! The word was {choosen_word}\n")
else:
    print(f'You lost :( The word was {choosen_word}\n')

