# Suppose we want to store some info about each person

names = ['Jaewook', 'Volodymr', 'Obama']

# This is clearly bad
jaewook_age = 18
volodymyr_age = 16
obama_age = 61

# (1) the list could be infinitely long
# (2) the names could be anything

# improved: parallel list
ages = [18, 16, 61]
for i in range(len(names)):
    print(f'{names[i]} is {ages[i]} years old')

# That's pretty good but it still relies on us knowing
# that the two lists are supposed to be associated
# Even better: a dictionary! A new data type!

# A dictionary associates each key with a value

person_to_age = {
    # keys       # values
    'Jaewook'   : 18,
    'Volodymyr' : 16,
    'Obama'     : 61
}

# Keys are just like indices, except they don't have to be 0, 1, 2 ...
# They can be strings or any number

# Look up a person's age

print(person_to_age['Jaewook'])

# Can you look up a person by age?
# You have to make the reverse dictionary

age_to_person = {
    18          : 'Jaewook',
    16          : 'Volodymyr',
    61          : 'Obama',
}

print(age_to_person[18])

# Can a key have more than one value?
# It can go to a list that can contain multiple values

person_to_data = {
    # keys       # values
    'Jaewook'   : [18, '123 Fake Street'],
    'Volodymyr' : [16, '576 Drury Lane'],
    'Obama'     : [61, 'White House'],
}

# Can you randomly pick a person from a dictionary?
# Yes! If you convert it to a list first

import random
name = random.choice(list(person_to_data))

# How do we get the data associated with a person?

# Extract the data
data = person_to_data[name]

# Extract the parts of the data
age = data[0]
address = data[1]

# Print
print(f'{name} is {age} and lives at {address}')

# Program: a li'l phonebook

name = input('Enter a name: ')

if name in person_to_data:
    data = person_to_data[name]
    age = data[0]
    address = data[1]

    print(f'{name} is {age} and lives at {address}')

else:
    print(f'{name} is not in the phonebook')

# Task: Make a dictionary of the students currently in the class.
# Keys are their names (like we've done before)
# Values are lists of three data points that you decide
# e.g. hair colour, favourite colour, height, weight, political party... make it up

pokedex = {
    # name            # profession, attack strength, colour
    'Mr. Sawczak'   : ['Teacher',   17,     'Purple'],
    'Christian'     : ['Student',   21,     'Green'],
    'Colin'         : ['Student',   28,     'Purple'],
    'Shane'         : ['Student',   5,      'Grue'],
    'Hogan'         : ['Student',   13,     'Brown'],
    'Josh Min'      : ['Student',   7,      'Green'],
    'Evan'          : ['Student',   10,     'Seven'],
    'Jack'          : ['Student',   20,     'Black'],
    'Julia'         : ['Student',   15,     'Teal'],
    'Josh Carone'   : ['Student',   998,    'Orange'],
    'Jaewook'       : ['Student',   70,     'Red'],
    'Volodymyr'     : ['Student',   14,     'Red'],
    'Brandon'       : ['Student',   21,     'Blue'],
    'Stephen'       : ['Student',   -1,     'Grey'],
    'Adrian'        : ['Student',   34,     'Purple'],
    'William'       : ['TA',        15000,  'Black'],
    'Fenchyl'       : ['Student',   76,     'White'],
    'Daniel'        : ['Student',   2,      'Blue'],
    'Dina'          : ['Student',   3,      'Brown'],
    'Selasie'       : ['Student',   4,      'Chartreuse'],
}
