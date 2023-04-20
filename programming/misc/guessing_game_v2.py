# Guessing game
import random

secret_number = random.randint(1, 100)

guess = int(input('Guess a number between 1 and 100: '))
n_guesses = 1

while secret_number != guess:

    if secret_number > guess:
        print("too low")
    else:
        print("too high")

    guess = int(input('Guess a number between 1 and 100: '))
    n_guesses += 1

print(f"Right!!! You took {n_guesses} guesses")
