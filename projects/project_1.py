def main():
    print('This project is about string manipulation')
    print('=========================================\n')
    user_name = input('What is your name: ')
    print(f'Hello {user_name}!\n')
    print('I will count the number of times that a specific letter occurs in a message.\n')
    message = input('Please eneter a message: ')
    letter = input('Which letter would you like to count the occurences of: ')
    print(f'\n{user_name}, your message has {message.lower().count(letter.lower())} {letter}\'s in it.')