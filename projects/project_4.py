import math
def main():
    print('This project is about math')
    print('==========================\n')
    print("Welcome to Right Triangle Solver App!\n")
    side1 = float(input('What is the first leg of the triangle: '))
    side2 = float(input('What is the second leg of the triangle: '))
    print(f'\nFor a trinangle with sides of {side1} and {side2},\
          the hypotenuse is {round(math.sqrt(pow(side1, 2) + pow(side2, 2)), 3)}')
    print(f'For a trinangle with sides of {side1} and {side2},\
          the area is {round(side1 * side2 / 2, 2)}')
