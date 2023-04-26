# for i in range loop to repeat code

chorus = "Peanut Butter Jelly Time"
for i in range(5):
    print(chorus)

# ponder: how is this different from a while loop?
# range loop is finite -- it has a definite end
# while loop is potentially infinite -- it can depend on what people do

# =============================================================================

# # # for i in range loop to access specific items

# # # e.g. every other item
text = input('Enter some text to make crazy: ')
crazy_text = ''

for i in range(len(text)):

    # check if i is even
    if i % 2 == 0:
        crazy_text += text[i].lower()
    else:
        crazy_text += text[i].upper()

print(crazy_text)

# =============================================================================

# # Task to practice this:
# # ask for text
# # make a string consisting of only every 3 letter, starting from 0
# # e.g. 'abcdefghijk' -> 'adgj'

# text = input('Enter some text to keep only 3rd letter: ')
# third_letters = ''

# for i in range(len(text)):

#     # only keep divisible by 3
#     if i % 3 == 0:
#         third_letters += text[i]
    
# # print(third_letters)

# =============================================================================

# Ask for some text
# Make a list of all the indices of spaces in the text
# e.g. 'John Matthew Mark Luke' -> [4, 12, 17]

text = input('Enter some text: ')
spaces = []

for i in range(len(text)):

    if text[i].isspace():
        spaces.append(i)

print(spaces)

# =============================================================================

# Using range loop to compare parallel strings

prompt = 'import os'
attempt = input(f'Type: {prompt}\n    : ')

for i in range(len(attempt)):

    if attempt[i] != prompt[i]:
        print(f'Mistake found at {i}')
        break # ends the loop

print('No mistakes found')
