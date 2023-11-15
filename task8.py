def find_largest(num1, num2, num3):

    largest = max(num1, num2, num3)

    return largest


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the function to find the largest number
result = find_largest(num1, num2, num3)

# Print the result
print("The largest number is:", result)
