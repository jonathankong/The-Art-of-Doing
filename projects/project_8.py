

import random as r

POSITIONS = {
    1 : 'point guard',
    2 : 'shooting guard',
    3 : 'small forward',
    4 : 'power forward',
    5 : 'centre'
}

def roster_print(players_dict):
    largest_pos_len = len(max(players_dict.values(), key=len))
    print(f'\t\tYour starting {len(players_dict)} for the upcoming basketball season:')
    for i in range(1, len(players_dict) + 1):
        print('\t\t{0:<{1}}\t\t{2}'.format(POSITIONS.get(i).title() + ':', largest_pos_len, players_dict.get(i)))

def main():
    print('This project uses dictionaries, max method, functions, and string formatting')
    print('===============================================================================================\n')
    players_dict = {
        1:'',
        2:'',
        3:'',
        4:'',
        5:'',
    }
    print('Welcome to the Basketball Roster Program\n\n')
    for i in range(1, len(players_dict) + 1):
        players_dict[i] = input(f'Who is your {POSITIONS.get(i)}: ').title()
    
    roster_print(players_dict)
    
    remove_player_ind = r.randint(1, len(players_dict))
    
    print(f'Oh no, {players_dict[remove_player_ind]} is injured.')
    print(f'Your roster only has {len(players_dict) - 1} players')
    players_dict[remove_player_ind] = input(f"Who will take {players_dict[remove_player_ind]}'s spot: ").title()
    
    roster_print(players_dict)

    print(f'Good luck {players_dict[remove_player_ind]} you will do great!\n\
          Your roster now has {len(players_dict)} players.')
