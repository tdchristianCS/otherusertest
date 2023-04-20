import random
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