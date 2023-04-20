import random

POPULATION = 1000
START_SICK = 10
DAYS = 30
CHANCE = 0.1

days = 0
n_sick = START_SICK
while days < DAYS and n_sick < POPULATION:
    for person in range(n_sick):
        if random.randint(0, 100) / 100 < CHANCE:
            n_sick += 1
    days += 1

print(f'After {days} days, {n_sick} people are sick')
            
