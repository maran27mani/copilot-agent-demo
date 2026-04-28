#!/usr/bin/env python3
"""
Simple Calculator Application
Supports basic arithmetic operations: add, subtract, multiply, and divide.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def is_numeric(value):
    """
    Validate if a string value can be converted to a number.
    
    Args:
        value (str): The string value to validate
        
    Returns:
        bool: True if the value is numeric, False otherwise
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def get_numeric_input(prompt):
    """
    Get and validate numeric input from user.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        float: The validated numeric input
    """
    while True:
        user_input = input(prompt).strip()
        if is_numeric(user_input):
            return float(user_input)
        else:
            print(f"Invalid input '{user_input}'. Please enter a valid number.")


def main():
    """Main calculator interface."""
    print("=" * 40)
    print("         Simple Calculator")
    print("=" * 40)
    
    while True:
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("\nEnter operation (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("\nThank you for using Calculator!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please try again.")
            continue
        
        num1 = get_numeric_input("Enter first number: ")
        num2 = get_numeric_input("Enter second number: ")
        
        try:
            if choice == '1':
                result = add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\nResult: {num1} × {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\nResult: {num1} ÷ {num2} = {result}")
        
        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
