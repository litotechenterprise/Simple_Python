
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
def addToTotal(total, num):
    return total + num

def getPizzaSize():
    if (size == "S"):
        return 15
    elif(size == "M"):
        return 20
    else:
        return 25

def AddPepper(total):
    if(add_pepperoni == "Y"):
        if(size == "S"):
            return addToTotal(total, 2)
        else:
            return addToTotal(total, 3)
    return total

price = 0
pizza = getPizzaSize()
price = addToTotal(price, pizza)
price = AddPepper(price)

if (extra_cheese == "Y"):
    price = addToTotal(price, 1)

print(f"Your final bill is: ${price}") 