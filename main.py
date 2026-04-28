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
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
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
        except ValueError:
            print(f"\nError: Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()
