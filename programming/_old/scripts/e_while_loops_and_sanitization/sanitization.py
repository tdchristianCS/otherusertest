# Validation: checking that input meets certain requirements, it's valid
# Sanitization: clean up input to make it meet certain requirements

# A form where people can enter their name
# Their name is only allowed to have letters, hyphens, and spaces
# Input their name, and output the sanitized version of their name

name = input('Enter your name: ')

# sanitize by string building

sanitized = ''

for char in name:
    if char.isalpha() or char in ' -':
        sanitized = sanitized + char

print(sanitized)



# some test cases (feel free to add your own)

# In:   Jacob Smith
# Out:  Jacob Smith

# In:   Jac0b 5mith
# Out:  Jacb mith

# In:   Anthony_Perella_27
# Out:  AnthonyPerella

# In:   Antonio Garcia-Marquez
# Out:  Antonio Garcia-Marquez

