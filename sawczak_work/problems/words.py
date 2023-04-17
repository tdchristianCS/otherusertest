# write a program that counts the number of words
# in a sentence the user enters
# words are defined as separated by spaces

# ====

# e.g. if they input 'my name is ryan'
# your program outputs 4

# ====

# hint: str.count exists
# e.g. 'robby'.count('b') -> 2

# ====

sentence = input('Enter a sentence: ')
n_words = sentence.count(' ') + 1
print(n_words)
