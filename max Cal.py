def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for the operation
    operation = input("Enter choice (1/2/3/4): ")

    # Check if the input is valid
    if operation not in ['1', '2', '3', '4']:
        print("Invalid input. Please select a valid operation.")
        return

    # Get user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if operation == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

# Run the calculator
calculator()