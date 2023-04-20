# Guessing game
import random

MAX_GUESSES = 6

secret_number = random.randint(1, 100)

guess = int(input('Guess a number between 1 and 100: '))
n_guesses = 1

while (secret_number != guess) and (n_guesses < MAX_GUESSES):

    if secret_number > guess:
        print("too low")
    else:
        print("too high")

    guess = int(input('Guess a number between 1 and 100: '))
    n_guesses += 1

if guess == secret_number:
    print(f"Right!!! You took {n_guesses} guesses")
else:
    print(f"You lost after {n_guesses} guesses! The number was {secret_number}.")
