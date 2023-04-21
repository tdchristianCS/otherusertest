# 1. What does this code do?
# 2. Give each variable a logical name
# 3. Write good input/print strings

# The code asks for two pieces of text.
# It then takes the first character of the first piece
# and the last character of the second piece,
# combines them, and prints the result.

text_1 = input('Enter text 1: ')
text_2 = input('Enter text 2: ')

first_and_last = text_1[0] + text_2[-1]

print(first_and_last)
