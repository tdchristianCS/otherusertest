# constants

POPULATION = 10000
START_SICK = 3
SPREAD = 5
DAYS = 30

# simulation
# every day, each sick person will infect SPREAD # of other people
# at the end of the simulation, report how many people got sick

# we need to keep track of how many are currently sick
currently_sick = START_SICK

for day in range(DAYS):
    for patient in range(currently_sick):
        currently_sick += SPREAD

        if currently_sick > POPULATION:
            currently_sick = POPULATION

    # Sstop simulation if entire pop is already all sick
    if currently_sick >= POPULATION:
        break # break instantly ends a loop early
    
    print(f'Day {day + 1}: {currently_sick} people sick')

# let's print out how many are sick
print()
print(f'After {day + 1} days, {currently_sick} people are sick')

