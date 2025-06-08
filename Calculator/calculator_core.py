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
        #  cli_calculator();
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
        #  cli_calculator()
    return n1 // n2