from clear import clear_terminal
hot_drinks = {
    "expresso":{
        "price":1.50,
        "recipe":{
            "water":50,
            "coffee":18
        }
    },
    "latte":{
        "price":2.00,
        "recipe":{
            "water":200,
            "coffee":24,
            "milk":150
        }
    },
    "cappuccino":{
        "price":3.00,
         "recipe":{
            "water":250,
            "coffee":24,
            "milk":100
         },
    },
}
coins = {
    'penny':0.01,
    'nickel':0.05,
    'dime':0.10,
    'quarter':0.25,
}


def printReport(item, qty):
    if item == "water":
        print(f"Water: {qty}ml")
    elif item == "coffee":
        print(f"Coffee: {qty}g")
    elif item == "milk":
        print(f"Milk: {qty}ml")
    else:
        print(f'Money: ${qty}')


def check_resources(inventory, choice):
    able = True
    for key in hot_drinks[choice]["recipe"]:
        if hot_drinks[choice]["recipe"][key] > inventory[key]:
            print(f"Sorry there isn't enough {key}")
            able = False

    return able

def remove_resource(inventory, recipe):
    for key in recipe:
        inventory[key] = inventory[key] - recipe[key]

    return inventory

def process_payment(price):
    print(f"Please enter ${price}")
    quarters_qty = int(input("How many quarters would you like to enter?: "))
    dimes_qty = int(input("How many dimes would you like to enter?: "))
    nickels_qty = int(input("How many nickels would you like to enter?: "))
    pennys_qty = int(input("How many pennys would you like to enter?: "))

    total_entered = (quarters_qty * coins["quarter"]) + (dimes_qty * coins["dime"]) + (nickels_qty * coins["nickel"]) + (pennys_qty * coins["penny"])
    if total_entered >= price:
        print(f"Here is your change {total_entered - price}")
        return True
    print("You did not enter sufficient funds")
    return False


    



def start():
    on = True
    machine_inventory = {
        "water":300,
        "milk":200,
        "coffee":100,
        "money":0.00
    }
    while on:
        choice = input("What would you like? (expresso, cappuccino or latte):  ")

        if choice == "off":
            on = False
            continue

        if choice == "report":
            for key in machine_inventory:
                printReport(key, machine_inventory[key]) 
        elif choice in hot_drinks:
            able  = check_resources(inventory=machine_inventory, choice=choice)
            if able:
                 paid = process_payment(hot_drinks[choice]["price"])
                 if paid:
                    machine_inventory["money"] = machine_inventory["money"] + hot_drinks[choice]["price"]
                    machine_inventory = remove_resource(machine_inventory, hot_drinks[choice]["recipe"])
                    print("Dispensing Coffee.....")
        else:
            print("Sorry we're unable to make that")

clear_terminal()
start()