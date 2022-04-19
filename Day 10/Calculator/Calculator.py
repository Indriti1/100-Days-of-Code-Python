from art import logo
from replit import clear


# Add function
def add(n1, n2):
    return (n1 + n2)


# Multiply function
def multiply(n1, n2):
    return (n1 * n2)


# Subtract function
def subtract(n1, n2):
    return (n1 - n2)


# Divide function
def divide(n1, n2):
    return (n1 / n2)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation.: ")

        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()