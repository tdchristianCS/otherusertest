# Everything that comes from input is a string
# So I must convert to an integer if that's what I want it to be
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

# In a script, unlike the shell, we don't get live feedback
# Instead, we are in a "black box" and we have to print
# whatever we want to see

# We need to CAST the integer to a string so it can be combined
# print('Your first number is ' + str(x))

# Incidentally, you can also convert both directions
# str(5) -> '5'
# int('5') -> 5

print('Adding x and y: ' + str(x + y))

# practice: try doing a few operations and printing the result

input('Enter to quit')
