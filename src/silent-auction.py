from asciiart import GAVEL
from clear import clear_terminal

print(GAVEL)
print("Silent Auction")

dic = {}

should_continue = True


def find_highest_bid(bids):
    max = 0
    leader = ""
    for name, bet in bids.items():
        if bet > max:
            leader = name
            max = bet

    print(f"{leader} has won the auction with a bid of ${max}")

while should_continue:
    name = input("Enter the auctioner name?:\n")
    bet = int(input("Enter the amount to bid:\n"))
    dic[name] = bet

    another = input("Is there another auctioner? type yes or no\n").lower()
    clear_terminal()
    if another == "no":
        should_continue = False
        find_highest_bid(dic)

    




        





