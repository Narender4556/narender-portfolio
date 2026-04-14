import random

guess = random.randint(1, 100)

while True:
    try:
        number = int(input('Guess the number: '))
        if number > guess:
            print('Too high!')
        
        elif number < guess:
            print('Too low!')
            
        else:
            print('Congratulation you guessed the number.')
            break
            
    except ValueError:
        print('Please enter a valid number!')
            

        
        
        
            