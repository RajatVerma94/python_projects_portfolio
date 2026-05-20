#Import the logo from the art library but don't print it yet, we want it printed everytime the user wants the
#calculator to start all over again
from art import logo

#Define the operation's functionalities so that we don't have to do this again and again
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Create a dictionary of all the operations for the user to choose from
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    #Take the inputs from the user about the n1 and n2. Also, about the operation that needs to be performed
    #Also, print out all the symbols for the user to chose from so, user don't chose an operation which is out of scope.

    num1 = float(input("Enter the first number: "))

    continue_calculation = True
    while continue_calculation:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Enter an operation symbol: ")
        num2 = float(input("Enter the second number: "))
        answer = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        #Now, we need to ask the user if they need to keep continuing or start the calculation all over again.
        #For continuing the calculation we will use the while loop, but we will keep num1 variable input outside the loop.
        #In the continuing case, answer becomes the num1

        choice = input("Type 'y' to continue calculating with the answer as your input for first number or type 'n' to restart the calculator: ").lower()
        if choice == "y":
            num1 = answer

        #If the user chooses to restart the calculation then we need to end the while loop and call the calculator function
        else:
            print("\n" * 20)
            continue_calculation = False
            calculator()

calculator()
