# Advanced Calculator with Error Handling

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    print("\nWelcome to the Advanced Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input! Please choose a valid option.")
            continue
        
        # Get two numbers from the user with error handling
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        # Perform the chosen operation
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")

if __name__ == "__main__":
    calculator()