
import random
from clear import clear_terminal
from asciiart import BLACKJACK
def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_cards_sum(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw 🥲\n"
    elif dealer_score == 0:
        return "Dealer has blackjack 😱\n"
    elif user_score == 0:
        return "User has blackjack 😎\n"
    elif user_score > 21:
        return "You went over, You lose 😭\n"
    elif dealer_score > 21:
        return "Dealer went over, You win 🤩\n"
    elif user_score > dealer_score:
        return "You win 🤑\n"
    else:
        return "You Lose 🤬\n"
    

def play_blackjack():
    print(BLACKJACK)
    is_game_over = False
    dict = {"dealer":[],"user":[]}
    d_sum = -1
    user_sum = -1
    for _ in range(2):
        dict["user"].append(deal_cards())
        dict["dealer"].append(deal_cards())

    while not is_game_over:
        d_sum = calculate_cards_sum(dict["dealer"])
        user_sum = calculate_cards_sum(dict["user"])
        print(f"your cards: {dict['user']}, current total: {user_sum}")
        print(f"Dealer first card is {dict['dealer'][0]}")
        if user_sum == 0 or d_sum == 0 or user_sum > 21 or d_sum > 21:
            is_game_over = True
        else:
            another = input("Hit?: type 'yes' or 'no': \n")
            if another == "yes":
                dict["user"].append(deal_cards())
            else:
                is_game_over = True

    while d_sum != 0 and d_sum < 17:
        dict["dealer"].append(deal_cards())
        d_sum = calculate_cards_sum(dict["dealer"])

    print(f"User final hand: {dict['user']}, final total: {user_sum}") 
    print(f"Dealer final hand: {dict['dealer']}, final total: {d_sum}") 
    print(compare(user_sum, d_sum))


keepPlaying  = True
while keepPlaying:
    clear_terminal()
    play_blackjack()

    again = input("Would you like to play again?: \n")
    if again == "no":
        keepPlaying = False