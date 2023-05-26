# samplecalculatore

# main math operations
def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

def calculator():
        # ask user for operation
        operation = input("choose an operation (+, -, *, /): ")
        # ask user for num1
        num1 = float(input("enter the first number"))
        # ask user for num2
        num2 = float(input("enter the second number"))