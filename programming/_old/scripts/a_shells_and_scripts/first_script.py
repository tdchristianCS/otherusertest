x = 5
y = 10

# In a script, unlike the shell, we don't get live feedback
# Instead, we are in a "black box" and we have to print
# whatever we want to see

# We need to CAST the integer to a string so it can be combined
print('Your first number is ' + str(x))

# Incidentally, you can also convert both directions
# str(5) -> '5'
# int('5') -> 5

print('Adding x and y: ' + str(x + y))

# practice: try doing a few operations and printing the result
