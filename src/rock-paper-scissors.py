import random
opts = [
 '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

 '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

 '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']



user_wins = 0
computer_wins = 0 

#Write your code below this line 👇


def return_winner(usr_wins, cpu_wins):
    if usr_wins > cpu_wins:
        return "User is Winning!!"
    elif cpu_wins > usr_wins:
        return "Computer is Winning!!"
    else:
        return "It's currently tied"


def play():
    global computer_wins, user_wins
    win = "You Win!"
    lose = "You lose!"  

    user = int(input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))


    computer = random.randint(0,2)
    print("User chose:")
    print(opts[user])
    print("Computer chose:")
    print(opts[computer])

    if user == 0 and computer == 2:
        user_wins += 1
        print(win)
    elif user == 0 and computer == 1:
        computer_wins += 1
        print(lose)
    elif user == 1 and computer == 0:
        user_wins += 1
        print(win)
    elif user == 1 and computer == 2:
        computer_wins += 1
        print(lose)
    elif user == 2 and computer == 0:
        computer_wins += 1
        print(lose)
    elif user == 2 and computer == 1:
        user_wins += 1
        print(win)
    else:
        print("Draw")

    winner = return_winner(user_wins, computer_wins)


    print(f"Count {user_wins} - {computer_wins}: {winner}\n")    

    again = input(
        "Play again? Y or N \n").upper()
    
    if again == "Y":
        play()
    
play()