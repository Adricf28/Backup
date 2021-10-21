import random
import time

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    contador = 0
    print(f'Trying to guess a number between 1 and {x}...')
    while guess != random_number and contador != 5:
        guess = random.randint(1,x)   # AUTOMATIC
        #guess = int(input(f'Guess a number between 1 and {x}.'))  # MANUAL
        time.sleep(0.7)
        print(guess)
        contador += 1
        time.sleep(0.3)
        if guess > random_number:
            print('Too high bitch')
        elif guess < random_number:
            print('Too low bitch')
        else:
            print(f'U got it, biaaaatch. The number was {random_number}')   
        
def computer_guess(x):
    number = int(input('Number u want the computer to guess: '))
    contador = 0
    guess2 = 0
    while guess2 != number and contador != 5:
       guess2 = random.randint(1,x)
       time.sleep(0.7)
       contador += 1
       print(guess2)
       time.sleep(0.3)
       if guess2 > number:
           print('Haha too high bobo')
       elif guess2 < number:
           print('Haha too low bobo')
       else:
           print(f'Fuck you, u got it. The number was {number}')
   
            
guess(20)
computer_guess(20)