# Create a function to play rock paper scissors with you
from random import randint

def rock_paper_scissors():
    user_choice = input('\n[1] Rock \n[2] Paper \n[3] Scissors \nChoice: ')
    # Convert users choice to an integer for comparison
    user_choice = int(user_choice)
    # Assign the computer a choice
    computer_choice = randint(1, 3)
    # Dictionary of choices
    options = {
        1 : 'Rock',
        2 : 'Paper',
        3 : 'Scissors',
    }
    # Display users and computers choice
    print(f'\nYou: {options[user_choice]}')
    print(f'Computer: {options[computer_choice]}\n')

    # Determine the result
    if user_choice == 1 and computer_choice == 2:
        print('You lose.')

    elif user_choice == 2 and computer_choice == 3:
        print('You lose.')

    elif user_choice == 3 and computer_choice == 1:
        print('You lose.')
    
    elif user_choice == computer_choice:
        print('Draw.')

    else:
        print('You win.')

rock_paper_scissors()