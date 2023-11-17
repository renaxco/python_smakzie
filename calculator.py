# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Main calculator loop
while True:
    # Menu for the user
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    # Take user input for operation choice
    user_input = input(": ")

    if user_input == "quit":
        break

    if user_input in ("add", "subtract", "multiply", "divide"):
        # Take user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation
        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
            print("Result:", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please enter a valid operation.")
