import random
from clear import clear_terminal
clear_terminal()
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")

if diff == "hard":
    lives = 5
else:
     lives = 10

answer = random.randint(1,100) 
is_game_over = False
Found = False

while not is_game_over and lives > 0:
     print(f"You have {lives} attempts remaining to guess the number.")
     guess = int(input("Make a guess: "))
     if guess == answer:
          print("You got it!!!")
          is_game_over = True
          Found = True
          break
     
     lives -= 1
     if lives == 0:
          continue

     if guess > answer:
          print("Too High.")
     else:
          print("Too Low.")
     print("Guess again.")


if Found:
     print("Winner!!!!!!!")
else:
     print("Sorry better luck next time 😪")