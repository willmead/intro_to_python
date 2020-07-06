"""
Calculator
Date: 28/03/20
Author: Will

An extensible calculator for teaching functions
"""

# Functions
def add(num1, num2):
    print(f"I am adding {num1} and {num2}")
    print(num1 + num2)

def subtract(num1, num2):
    print(f"I am subtracting {num2} from {num1}")
    print(num1 - num2)

def multiply(num1, num2):
    print(f"I am multiplying {num1} by {num2}")
    print(num1 * num2)

def divide(num1, num2):
    print(f"I am dividing {num1} by {num2}")
    print(num1 / num2)


# Main Program
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
operation = input("Do you want to +, -, * or /?")

if operation == "+":
    add(num1, num2)
elif operation == "-":
    subtract(num1, num2)
elif operation == "*":
    multiply(num1, num2)
elif operation == "/":
    divide(num1, num2)
else:
    print("I didn't understand that.")
