# 1. What does this code do?
# 2. Give each variable a logical name
# 3. Write good input/print strings

# The code asks you to enter some text and a term
# to search for. It then checks if the search term
# occurs in the text. If so, it prints how many times
# it occurs. If not, it tells you so.

text = input('Enter some text: ')
search_term = input('Enter a term to search for: ')

if search_term in text:
    print(text.count(search_term))
else:
    print('No occurrences found')

