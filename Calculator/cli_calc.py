from calc_ascii import GenerateCalculatorArt
import os

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Divide
def divide(n1, n2):
    if n2 == 0:
        print("Error: Cannot divide by zero")
        cli_calculator();
    return n1 / n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Exponential
def exponentiate(n1, n2):
    return n1 ** n2

# Modulo
def modulus(n1, n2):
    return n1 % n2

# Floor division
def floor_divide(n1, n2):
    if n2 == 0:
        print("Error: Cannot divide by zero")
        cli_calculator();
    return n1 // n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "**": exponentiate,
    "%": modulus,
    "//": floor_divide,
}

def Check_Valid_Number(number):
    while True:
      try:
          return float(input(number))
      except ValueError:
              print("Please choose an appropriate number!")


def cli_calculator():
  
    calculator_running = True
    
    while calculator_running:
        
        GenerateCalculatorArt()  
        
        num1 = Check_Valid_Number("What is the first number? ")

        for key in operations:
            print(key)

        while True:
            operation_symbol = input("Pick an operation: ")
            
            if operation_symbol not in operations:
                print("Please choose an operation from the options!")
                continue; 
            
            num2 = Check_Valid_Number("What is the next number? ")

            chosen_operation = operations[operation_symbol]
            answer = chosen_operation(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            user_choice = input(f"Would you like to continue calculating with {answer}? (type 'y'), or type 'n' to restart, or 'q' to quit: ").lower()

            if user_choice == 'n':
                os.system('cls')
                break
            if user_choice == 'q':
                return
            else:
                num1 = answer