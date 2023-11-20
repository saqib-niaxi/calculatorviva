def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

import math

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Invalid input for square root"

def calculator():
    print("Welcome to the Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exit")

    while True:
        choice = input("Enter choice (1-6): ")

        if choice in ('1', '2', '3', '4', '5'):
            if choice == '5':
                num = float(input("Enter number: "))
                print("Result:", square_root(num))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))
        elif choice == '6':
            print("Exiting the Calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

calculator()