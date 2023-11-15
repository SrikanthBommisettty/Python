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
    # Check if the denominator is not zero
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Function to perform modulus
def modulus(x, y):
    # Check if the denominator is not zero
    if y != 0:
        return x % y
    else:
        return "Cannot calculate modulus with zero denominator"

# Function to perform exponentiation
def exponentiate(x, y):
    return x ** y

# Function to perform floor division
def floor_divide(x, y):
    # Check if the denominator is not zero
    if y != 0:
        return x // y
    else:
        return "Cannot perform floor division by zero"

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations and display the results
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Modulus:", modulus(num1, num2))
print("Exponentiation:", exponentiate(num1, num2))
print("Floor Division:", floor_divide(num1, num2))
