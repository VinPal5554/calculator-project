
# Calculator Project

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}


def calculator():
    num1 = float(input("What is the first number?"))

    for key in operations:
        print(key)

    calculator_running = True

    while calculator_running:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?"))

        chosen_operation = operations[operation_symbol]
        answer = chosen_operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart: ").lower()

        if user_choice == 'n':
            calculator_running = False
            calculator()
        else:
            num1 = answer


calculator()