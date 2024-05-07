# Perform the selected operation
def add(a, b):
    """Addition operation."""
    return a + b

def subtract(a, b):
    """Subtraction operation."""
    return a - b

def multiply(a, b):
    """Multiplication operation."""
    return a * b

def divide(a, b):
    """Division operation."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
#Display the menu with the available operations (Addition, Subtraction, Multiplication, Division).

# Ask the user to choose an operation 

# If the choice is invalid, display an error message and go back to the first step.

# Ask the user for two numbers

# Display the result.

# Ask the user if they want to perform another calculation.

# Handle Exceptions