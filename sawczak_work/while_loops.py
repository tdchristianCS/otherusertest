# infinite loop -- always true
# have to kill terminal to avoid crashing

# i = 0
# while True:
#     i = i + 1
#     print(i)


# input-based loop -- uses a CONDITION to determine whether to repeat or not

# import random
# secret = random.randint(1, 100)

# guess = int(input('Guess a # between 1 and 100: '))
# while guess != secret:

#     if guess > secret:
#         print('Lower')
#     else:
#         print('Higher')
        
#     guess = int(input('Guess a # between 1 and 100: '))

# print('Right')

# while until you quit

# choice = input('Type Q to quit: ').upper().strip()
# while choice != 'Q':
#     choice = input('Type Q to quit: ').upper().strip()
# print('Quitting')

# combine those for infinitely replayable game

import random

print('Welcome to the guessing game!')
print()

choice = ''
while choice != 'Q':
    secret = random.randint(1, 100)

    guess = int(input('Guess a # between 1 and 100: '))
    while guess != secret:

        if guess > secret:
            print('Lower')
        else:
            print('Higher')
            
        guess = int(input('Guess a # between 1 and 100: '))

    print('Right')

    print()
    choice = input('Hit Enter to play again or Q to quit: ').upper().strip()
print('Quitting')







# gender = input('Enter your gender (M/F): ').lower().strip()

# if gender == 'm':
#     print('Hello, sir')

# elif gender == 'f':
#     print('Hello, ma\'am')

# else:
#     print('Our website cannot cope with your choice yet')
