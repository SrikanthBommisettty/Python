def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Get user input for the number
number = int(input("Enter a number to find its factorial: "))

# Check if the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the factorial function and print the result
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")
