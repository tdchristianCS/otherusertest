# 1. What does this code do?
# 2. Give each variable a logical name
# 3. Write good input/print strings

# The code asks the user to enter names repeatedly,
# until they type Q to quit.
# For each thing they enter, if it's alphabetic,
# it's added to a list of names.
# At the end, it prints out all the valid names.

names = []

choice = input('Enter a name or Q to quit: ')
while choice.upper() != 'Q':

    # If it's alphabetic (uses only A-Z)
    if choice.isalpha():
        # Capitalize it (title case) and add it to the list
        names.append(choice.title())

    choice = input('Enter a name or Q to quit: ')

# Print each name on its own line
print(f'Valid names:')
for name in names:
    print(name)
