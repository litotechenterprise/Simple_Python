from asciiart import CALCULATOR
from clear import clear_terminal



def addition(n1,n2):
    return n1 + n2
def subtraction(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1 / n2
def modulo(n1,n2):
    return n1 % n2
operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "%": modulo,
}

print(CALCULATOR)
should_continue = True

while should_continue:
    first_number = int(input("What's the first number?:  "))
    print("""
    +
    -
    *
    /
    %
        """)
    operation = input("Pick an operation: ")
    if operation not in operations:
        clear_terminal()
        print("invalid operation selected")
        
        continue
    second_number = int(input("What's the second number:  "))

    


    results = operations[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {results} \n")
    another = input("Would you like to make another operation?: type 'yes' or 'no' \n").lower()
    if another == "no":
        should_continue = False
    clear_terminal()





