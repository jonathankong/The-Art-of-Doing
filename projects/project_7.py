import csv
from pathlib import Path

def main():
    #current path
    print(Path.cwd())
    output_path = Path(f'{Path.cwd()}/project_7_extra_files/grocery_list').with_suffix('.csv')
    #creating directories while ignoring the file at the end of the path
    output_path.parents[0].mkdir(exist_ok=True, parents=True)
    #if (not output_path.exists()):
    with output_path.open(mode='a+') as grocery_list:
        wr = csv.writer(grocery_list, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        wr.writerow(['Spam'] * 5 + ['Baked Beans'])
        wr.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    