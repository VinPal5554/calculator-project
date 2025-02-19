import tkinter as tk


# Calculator Project


def GenerateCalculatorArt():
    print("""_________________________________________________________________________    
             / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ 
            | |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |
            | |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ < 
             \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_\ \n""")
             


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

# Exponential
def exponentiate(n1, n2):
    return n1 ** n2

# Modulo
def modulus(n1, n2):
    return n1 % n2

# Floor division
def floor_divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
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

# GUI Calculator
def on_click(value):
    current_text = entry_var.get()

    if value == "=":
        try:
            result = eval(current_text, {"__builtins__": None}, operations)
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif value == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + str(value))



def cli_calculator():
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
            cli_calculator()
        else:
            num1 = answer


def gui_calculator():
    global entry_var  # Ensure the entry variable is accessible inside the function
    root = tk.Tk()
    root.title("Calculator")

    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        ("7", "8", "9", "/"), ("4", "5", "6", "*"),
        ("1", "2", "3", "-"), ("C", "0", "=", "+")
    ]

    for r, row in enumerate(buttons):
        for c, char in enumerate(row):
            btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2, command=lambda v=char: on_click(v))
            btn.grid(row=r+1, column=c)

    root.mainloop()


# Choose Mode
def main():
    choice = input("Choose mode: Type 'cli' for command line or 'gui' for graphical interface: ").strip().lower()
    if choice == "cli":
        GenerateCalculatorArt();
        cli_calculator()
    elif choice == "gui":
        GenerateCalculatorArt();
        gui_calculator()
    else:
        print("Invalid choice! Please enter 'cli' or 'gui'.")
        main()

# Run program
main()




