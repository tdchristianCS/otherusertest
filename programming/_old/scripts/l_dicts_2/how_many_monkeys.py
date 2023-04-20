# Monkeys at typewriters
# Wikipedia: Infinite monkey theorem

import random

letters = 'abcdefghijklmnopqrstuvwxyz' + ' ' * 5 # 5 spaces to balance it out
hamlet_words = ['hamlet', 'denmark', 'words', 'to be', 'bodkin']

text = ''

N_LETTERS = 1000000

for i in range(N_LETTERS):
    text += random.choice(letters)

for word in hamlet_words:
    print(f'Looking for {word}')
    if word in text:
        print('Found it!!')
    else:
        print('No luck')
    
print('\n'  + text[:200] + '...')

