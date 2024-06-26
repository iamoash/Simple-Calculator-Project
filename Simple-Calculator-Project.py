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
def main():
    try:
        while True:
            print("Choose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
# Ask the user to choose an operation 
            choice = int(input("Enter your choice (1/2/3/4): "))
# If the choice is invalid, display an error message and go back to the first step.
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                continue
            # Ask the user for two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
# Display the result.
            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)

            print(f"Result: {result}")
# Ask the user if they want to perform another calculation.
            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation.lower() != "yes":
                print("Thank you, Love You!!")
                break
# Handle Exceptions
    except ValueError as e:
        print(f"Error: {e}")
        main()  # Restart the calculator if an error occurs

if __name__ == "__main__":
    main()
