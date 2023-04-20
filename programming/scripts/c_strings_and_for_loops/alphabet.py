first_word = input('Enter a word: ')
second_word = input('Enter another word: ')

# uppercase to normalize
if first_word.upper() < second_word.upper():
    print(first_word + ' comes first in the dictionary.')
elif second_word.upper() < first_word.upper():
    print(second_word + ' comes first in the dictionary.')
else:
    print('Why did you enter the same word twice?')

# ord and chr... play around with them
