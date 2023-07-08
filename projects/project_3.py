def main():
    print('This project is about variable types, rounding and math')
    print('=======================================================\n')
    print('Welcome to the Temperature Conversion Program\n')
    temp = float(input('What is the given temperature in degrees Fahrenheit: '))
    print(f'\nDegrees Fahrenheit:\t{temp}')
    print(f'Degrees Celsius:\t{round((temp - 32) * 5/9, 2)}')
    print(f'Degrees Kelvin:\t\t{round((temp - 32) * 5/9 + 273.15, 2)}')