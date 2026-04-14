import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK : '🪨', PAPER : '📃', SCISSORS : '✂️'}
choices = tuple(emojis.keys())
         
def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissors (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choices')
             
            
def display_choices(user_choice, computer_choice):
    print(f'User choice {emojis[user_choice]}')
    print(f'computer_choice{emojis[computer_choice]}')

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')    
    elif (
        (user_choice == 'ROCK' and computer_choice == 'SCISSORS') or 
        (user_choice == 'SCISSORS' and computer_choice == 'PAPER') or
        (user_choice == 'PAPER' and computer_choice == 'ROCK')):
        print('You win!')
    else:
        print('you lose')
        
def game_play():      
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        winner(user_choice, computer_choice)  
        should_continue = input('Continue (y/n): ').lower()
        if should_continue == 'n':
            break   
game_play()