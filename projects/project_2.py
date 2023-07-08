def main():
    print('This project is about variable types, rounding and math')
    print('=======================================================\n')
    print('Welcome to the MPH to MPS Conversion App\n')
    mph = float(input('What is your speed in miles per hour: '))
    miles_to_meters = 1609.34
    hours_to_secs = 3600
    print(f'Your speed in meters per second is {round(mph * miles_to_meters / hours_to_secs, 2)}')
    