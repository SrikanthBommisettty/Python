# Function to print a star pattern
def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Get the number of rows from the user
num_rows = int(input("Enter the number of rows for the star pattern: "))

# Call the function to print the star pattern
print_star_pattern(num_rows)
