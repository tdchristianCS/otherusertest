# We saw before that we can create as many variables as we want

colour_jacob = 'blue'
colour_anthony = 'green'
colour_mickey = 'red'

# But with an arbitrary # of variables, we want a list so we can dynamically
# append, remove, etc....

colours = ['blue', 'green', 'red']

# However, what did we lose?
# We lost the IDENTITY of each value!
# Which we had when it was a variable name

# So the solution is...

# dictionary (dict)

d = {
    'mickey': 'red',
    'anthony': 'green',
    'jacob': 'blue',
    'joyce': 'black'
}

print(d['joyce']) # black

d['dan'] = 'yellow'

# looping through keys

for key in d:
    print(key)

# looping through values

for key in d:
    print(d[key])
    
# looping through both

for key in d:
    print(f'{key}: {d[key]}')
    
