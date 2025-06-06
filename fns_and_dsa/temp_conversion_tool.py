CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature_value = (input('Enter the temperature to convert: '))
if temperature_value.isdigit():
    temperature_value = int(temperature_value)
else:
    print('Invalid temperature. Please enter a numeric value.')
    temperature_value = None

temperature_type = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()
if temperature_type.isalpha():
    match temperature_type:
        case 'C':
            result = convert_to_fahrenheit(temperature_value)
            print(f'{temperature_value}{"°"}{temperature_type} is {result:.13f}{"°"}F')
        case 'F':
            result = convert_to_celsius(temperature_value)
            print(f"{temperature_value} {"°"}{temperature_type} is {result:.13f}{"°"}C")           
        case _:
            print("Did you mean 'C' for celcius or 'F' for fahrenheit? \nTry again")
else:
    print('Invalid Input, try letter of the alphabet.')
    temperature_type = None