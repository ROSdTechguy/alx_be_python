# match_case_calculator.py

# Prompt the user for two numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Prompt the user for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation using match-case
match operation:
    case '+':
        result = first_number + second_number
    case '-':
        result = first_number - second_number
    case '*':
        result = first_number * second_number
    case '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero is not allowed."
    case _:
        result = "Error: Invalid operation."

# Print the result
print(f"The result is: {result}")
