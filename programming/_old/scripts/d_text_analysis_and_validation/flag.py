# HINT: Flags
# a flag is a True/False variable you use to track whether something happened

have_seen_space = False # start the flag at False, i.e. no spaces yet

text = input('Enter some text: ')
for char in text:
    if char == ' ':
        have_seen_space = True # I saw a space! set the flag to True

# finally, if the flag was set at any point, make a choice
if have_seen_space:
    print('There was a space somewhere!')
else:
    print('I never saw no spaces.')
    

# HINT: String length

# use len(string) to get the length as an integer
# >>> len('hello')
# 5


# HINT: Elimination

# Save the valid answer for the very end
# Check everything that could make it invalid, and print 'Invalid'
# At the end, if you haven't gotten any invalids, THEN print 'Valid'


# HINT: Result (this is a version of the flag hint)

# Use a result variable to store the current result
# And save to make you only print it once at the end

result = 'Valid'

if problem:
    result = 'Invalid'

if other_problem:
    result = 'Invalid'

print(result)


