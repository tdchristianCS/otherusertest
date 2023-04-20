### take user input and count the number the words
##sentence = input('Enter a sentence: ')
##words = sentence.split()
##n_words = len(words)
##print(n_words)
##
### list comprehension (listcomp)
##print(list(word for word in L if len(word) > 1))

# sum of a list
L = [5, 6, 7, 115, 151, 591]
total = 0
for item in L:
    total += item
print(total)

# modify that code slightly
# so that it takes input from a user
# and sums that input

# here's how you'll ask for input:
# they type in one number at a time
# add each number into a list (use the append list method)
# when they type Q you stop asking
# then you sum the list
# and print the total

user_numbers = [] # start by creating an empty list to store our numbers
next_int = input('Enter a number or Q to quit: ') # ask for an integer or Q
while next_int.upper().strip() != 'Q':
    if next_int.isdigit(): # make sure what they entered is a digit (optional)
        user_numbers.append(int(next_int)) # add the number to the list    
    next_int = input('Enter a number or Q to quit: ')

# now let's sum
total = 0
for item in user_numbers:
    total += item
print(total)

# here is where you should sum their numbers & output the sum


