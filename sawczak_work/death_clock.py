# basic human years
lifespan = 80

name = input('Enter your name: ')

# ask user age
age = int(input('Enter your age: '))

# ask pizzas
pizzas = int(input('Enter # of meals that are pizza per week: '))

# ask vitamins
vitamins = int(input('Enter # of vitamins per day: '))

# add 3 more factors of your choosing (all numerical for now)

checkups = int(input('Enter # of doctor visits per year: '))
salads = int(input('Enter # of salads per week: '))
smoking = int(input('Enter # of packs of cigarettes smoked per week: '))

# can we ask a yes/no question?
# we can hack it by treating it as a number
walking_allergy = int(input('Rate your allergy to walking with your actual feet? 1-10 '))

# years left
remaining = lifespan - age - (0.2 * pizzas) + (0.5 * vitamins) + (0.25 * checkups) + (0.2 * salads) - (1 * smoking) - (1.5 * walking_allergy)

print(f'{name}, you have {remaining} years left to live.')
