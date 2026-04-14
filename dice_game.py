import random

while True:
    user_choice = input('Roll the dice (y/n): ').lower()
    
    if user_choice in ['y', 'yes']:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f'({die1}, {die2}) → Total: {total}')
        
    elif user_choice in ['n', 'no']:
        print('Thanks for playing.')
        break
        
    else:
        print('Invalid choice. Please enter y or n.')