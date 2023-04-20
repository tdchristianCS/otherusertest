# How to have randomness

import random

# print(dir(random))
# There are a lot...
# The most useful 3...

# random.choice picks a random item from a container
names = ['Sean', 'Jean', 'Dean', 'Brian', 'Ryan']
print(random.choice(names))

# random.shuffle shuffles the order of items in a container
random.shuffle(names)
print(names)

# random.randint gives you a number between A and B inclusive
n = random.randint(1, 100)
print(n)
