import random

def main():

    n = random.randint(1, 100)
    print('I have picked a number between 1 and 100.')
    print()

    guesses = 1
    guess = int(input('Guess: '))
    while guess != n:
        if guess < n:
            print('Too high')
        else:
            print('Too low')
        print()
        guesses += 1
        guess = int(input('Guess: '))

    input('You guessed it in ' + str(guesses) + ' guesses!')


