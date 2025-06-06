# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Ensure the input is a positive integer
if size > 0:
    # Initialize the row counter
    row = 0
    while row < size:  # Iterate through each row
        for col in range(size):  # For each column in the current row
            print("*", end="")  # Print asterisks on the same line
        print()  # Move to the next line after completing the row
        row += 1  # Increment the row counter
else:
    print("Invalid input. Please enter a positive integer.")

