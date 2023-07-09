import math

def main():
    print('This project is about list manipulation')
    print('=======================================\n')
    print('Welcome to the Grade Sorter App\n')
    grade_list = []
    grade_list.append(int(input('What is your first grade (0 - 100): ')))
    grade_list.append(int(input('What is your second grade (0 - 100): ')))
    grade_list.append(int(input('What is your third grade (0 - 100): ')))
    grade_list.append(int(input('What is your forth grade (0 - 100): ')))

    print(f"\nYour grades are: [{str(grade_list)[0:]}]")
    grade_list.sort(reverse=True)
    print(f"\nYour grades from highest to lowest are: [{str(grade_list)[0:]}]")
    print(f'\nThe lowest two grades will now be dropped.')
    print(f'Removed grade: {grade_list[-1]}')
    grade_list.pop()
    print(f'Removed grade: {grade_list[-1]}\n')
    grade_list.pop()
    print(f"Your remaining grades are: [{str(grade_list)[0:]}]")
    print(f'Nice work! Your highest grade is a {grade_list[0]}')