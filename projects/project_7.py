import csv
from pathlib import Path
from datetime import datetime

def main():
    #destination path
    output_path = Path(f'{Path.cwd()}/project_7_extra_files/grocery_list').with_suffix('.csv')
    #creating directories while ignoring the file at the end of the path
    output_path.parents[0].mkdir(exist_ok=True, parents=True)

    try:
        # #get sample text and sniff the dialect of the csv file
        # with output_path.open(newline='') as file:
        #     sample = file.read(64)
        #     deduced_dialect = csv.Sniffer().sniff(sample)
        #     #read file fully
        # with output_path.open(newline='') as file:
        #     #list wrapper makes 2d array so reverting it back to 1d array
        #     grocery_list = list(csv.reader(file, deduced_dialect))[0]
        with output_path.open(newline='') as file:
            #list wrapper makes 2d array so reverting it back to 1d array
            grocery_list = list(csv.reader(file))
            if len(grocery_list) > 1:
                grocery_list = grocery_list[0]
    except FileNotFoundError as err:
        print("Grocery list doesn't exist. Creating empty list...")
        with output_path.open(mode='w', newline='') as file:
            pass
        grocery_list=[]
    
    dt_now = datetime.now()
    dt = dt_now.strftime("%d/%m/%Y %H:%M:%S")

    print(f'''Welcome to the Grocery App  
        Current Date and Time: {dt}
        You currently have {
            ', '.join(grocery_list[0:-1]) + 'and ' + grocery_list[-1]
            if len(grocery_list) > 1
            else 'nothing'
        } in your list''')
    
    answer = input("Type the food you'd like to add to your grocery list (Type 'n' to stop): ")

    while answer.lower() != 'n':
        grocery_list.append(answer)
        answer = input("Type the food you'd like to add to your grocery list (Type 'n' to stop): ")
    
    print(f'Here is your grocery list: \n{str(grocery_list)}')
    grocery_list.sort()
    print(f'Here is your grocery list sorted: \n{str(grocery_list)}')

    print('\nSimulating grocery shopping...\n')

    #Allow user to remove items
    while len(grocery_list) > 2:
        print(f'Current grocery list: {len(grocery_list)}')
        print(str(grocery_list))
        answer = input('What food did you just buy? ').lower()
        try:
            grocery_list.remove(answer)
            print(f'Removing {answer} from list...')
        except ValueError as ve:
            print(f'You did not have {answer} in your grocery list.')
        
    #Replace last item with another
    if len(grocery_list) == 0:
        print('You have no items in your grocery list. Please fill it in next time!')
    else:
        print(f'\nSorry, the store is out of {grocery_list[-1]}')
        grocery_list.pop()
        answer = input('What food would you like instead? ').lower()
        grocery_list.insert(0, answer)
        print(f'\nHere is what remains on your grocery list: \n{str(grocery_list)}')

        #Saving list
        print('Saving list...')
        with output_path.open(mode='w', newline='') as file:
            wr = csv.writer(file)
            wr.writerow(grocery_list)
        print('Complete')