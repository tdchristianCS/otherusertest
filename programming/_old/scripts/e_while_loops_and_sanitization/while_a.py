# while loops

# for loops let us do something a fixed # of times

for i in range(10):
    print('Hello!')

# while loops let us do something UNTIL A CONDITION IS MET

# we can use it to let a user quit a program

user_choice = input('Enter to print hello or Q to quit: ')
while user_choice.strip().upper() != 'Q':
    print('hello')
    user_choice = input('Enter to print hello or Q to quit: ')

print('OK! Have a good day')

# let's do something slightly more interesting

import random

user_choice = input('Enter for a random # or Q to quit: ')
while user_choice.strip().upper() != 'Q':
    print(random.randint(0, 100))
    user_choice = input('Enter for a random # or Q to quit: ')

print('great! byeee~~~')

# we can also use while to validate input

user_choice = input('Enter a number: ').strip()
while not user_choice.isdigit():
    print('Hey!!! You were supposed to enter a number >:(')
    user_choice = input('Enter a number: ').strip()

print('The number you picked was ' + user_choice)


# we can make the guessing game

secret_number = random.randint(0, 100)
user_choice = int(input('Guess a number between 0 and 100: '))
while user_choice != secret_number:
    print('You guessed incorrectly')
    user_choice = int(input('Guess a number between 0 and 100: '))

print('Correct!')

# let's make our guessing game more friendly to the user
# it's going to say whether our guess was too high or too low

tries = 1
secret_number = random.randint(0, 100)
user_choice = int(input('Guess a number between 0 and 100: '))
while user_choice != secret_number:
    if secret_number > user_choice:
        print('Too low')
    elif secret_number < user_choice:
        print('Too high')

    tries += 1    
    user_choice = int(input('Guess a number between 0 and 100: '))

print(f'Correct! Guessed in {tries} tries.')

