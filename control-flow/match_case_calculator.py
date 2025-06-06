# match_case_calculator
Numb1 = int(input("Enter the first number: "))
Numb2 = int(input("Enter the second number: "))
Operation = input("Choose the operation (+, -, *, /): ")

match Operation:
    case "+":
        print(Numb1 + Numb2)
    case "-":
        print(Numb1 - Numb2)
    case "*":
        print(Numb1 * Numb2)
    case "/":
        if Numb2 != 0:
            print(Numb1 / Numb2)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation selected.")
