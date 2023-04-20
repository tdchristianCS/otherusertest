# imports

import random

# constants

POPULATION = 10000
START_SICK = 3
SPREAD = 5
DAYS = 30
CHANCE = 0.1 # % chance (0.1 = 10%)

# simulation

# every day, each sick person will infect SPREAD # of other people
# at the end of the simulation, report how many people got sick

# we need to keep track of how many are currently sick
currently_sick = START_SICK

for day in range(DAYS): # for every day...
    for spreader in range(currently_sick): # for every sick person...
        for spreadee in range(SPREAD): # for every possible new sick person...

            # roll a die, and if it's within CHANCE add to the sick count
            die_roll = random.randint(0, 100) / 100
            if die_roll < CHANCE:
                currently_sick += 1

            if currently_sick > POPULATION:
                currently_sick = POPULATION

    # Daniel's idea: stop simulation if pop is already all sick
    if currently_sick >= POPULATION:
        break # break instantly ends a loop early
    
    print(f'Day {day + 1}: {currently_sick} people sick')

# let's print out how many are sick after the whole thing
print()
print(f'After {day + 1} days, {currently_sick} people are sick')

