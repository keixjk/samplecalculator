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
    try:
        # ask user for operation
        operation = input("choose an operation (+, -, *, /): ")
        # ask user for num1
        num1 = float(input("enter the first number"))
        # ask user for num2
        num2 = float(input("enter the second number"))

        # perform the input operation and numbers
        if operation == "+":
             result = add(num1, num2)
        elif operation == "-":
             result = subtract(num1, num2)
        elif operation == "*":
             result = multiply(num1, num2)
        if operation == "/":
             result = divide(num1, num2)
        else:
             print("Invalid operation")
             return
        
        # print result
        print("Result:", result)

        # ask user to try again or not
        choice = input("Do you want to try again? (yes/no): ")
        if choice.lower() == "yes":
             calculator()
        else: 
            print("Thank you!")
    # check for value errors
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        calculator()
    # check for zero division error
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        calculator()