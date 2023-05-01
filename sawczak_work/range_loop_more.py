# more for i in range loops

# triangles

for i in range(5):
    print('*' * (i + 1))

# triangle names!!

# e.g. name is 'Daniel'
# output is
# D
# aa
# nnn
# iiii
# eeeee
# llllll

# hint: 'D' is 'Daniel'[0]. 'a' is 'Daniel'[1]. etc.

name = input('Enter your name: ')
for i in range(len(name)):
    print(name[i] * (i + 1))

# range loops to enumerate possibilities

# first, what is chr

for i in range(26):
    print(chr(i + 65))

# now combine letters and numbers

for i in range(3):
    letter = chr(i + 65)

    for j in range(3):
        number = j + 1

        print(f'{letter}{number}')

# third level of nesting???

for i in range(26):
    letter_1 = chr(i + 65)

    for j in range(9):
        number = j + 1

        for k in range(26):
            letter_2 = chr(k + 97)

            print(f'{letter_1}{number}{letter_2}')

# TASK

# More triangle names
# e.g. if the name was 'Dan'

# We did this

'D'
'aa'
'nnn'

# Your job #1:
'nnn'
'aa'
'D'

# Your job #2:
'D'
'aa'
'nnn'
'aa'
'D'
