# This is a "The Game" simulator
# A certain number of people start as players of The Game
# If they "spread", i.e. talk to someone else
# they convert that person into a player of The Game
# sometimes people lose interest, though, and stop playing
# The Game ends once a certain number of people are players

# first thing in a file is any imports

import time
import random

# capital variables are called "constants"
# defined right after the imports
# they are not intended to change during execution
# these are like your "settings" for the game

POPULATION = 15_000
MAX_PLAYERS = POPULATION * 2/3
INITIAL_PLAYERS = 1

# some numbers to be used in a random formula for how much the player count spreads
# try changing these to see how it affects the game duration
SPREAD_FACTOR_1 = 5
SPREAD_FACTOR_2 = 2
SPREAD_FACTOR_3 = 4

# normal variables are the ones that change
# we initialize these at 0
current_players = INITIAL_PLAYERS
current_day = 0

# The simulation runs until the maximum number of players is reached
while current_players < MAX_PLAYERS:
    current_day = current_day + 1

    # random formula
    spread_multiple = ((random.randint(1, SPREAD_FACTOR_1) * SPREAD_FACTOR_2) / SPREAD_FACTOR_3)
    current_players = round(current_players * spread_multiple)

    # prevent going to 0
    if current_players == 0:
        current_players = 1

    # daily report
    print()
    print(f'It is day {current_day} and {current_players}/{POPULATION} people are players')
    time.sleep(0.5)

print('Simulation ended')
