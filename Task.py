def add(num1, num2):
    """
    Adds two numbers and returns the result.
    """
    return num1 + num2

def sub(num1, num2):
    """
    Subtracts the second number from the first and returns the result.
    """
    return num1 - num2

def prod(num1, num2):
    """
    Multiplies two numbers and returns the result.
    """
    return num1 * num2

def divide(num1, num2):
    """
    Divides the first number by the second and returns the result.
    Raises a ValueError if the second number is zero.
    """
    if num2 == 0:
        raise ValueError("Division by zero is not allowed")
    return num1 / num2

def main():
    """
    Main function to perform basic arithmetic operations based on user input.
    Continues to prompt the user for input until they choose to exit.
    """
    while True:
        try:
            # Get input from the user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter the operator (+, -, *, /): ")

            # Perform the chosen operation
            if op == "+":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif op == "-":
                print(f"{num1} - {num2} = {sub(num1, num2)}")
            elif op == "*":
                print(f"{num1} * {num2} = {prod(num1, num2)}")
            elif op == "/":
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid operator. Please try again.")
        except ValueError as e:
            # Handle invalid input
            print(f"Error: {e}")

        # Ask the user if they want to continue
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != "yes":
            break

if __name__ == "__main__":
    main()
