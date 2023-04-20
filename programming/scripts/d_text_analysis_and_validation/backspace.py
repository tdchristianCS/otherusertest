text = input('Enter some text. < is a backspace: ')

# String building
# Where you build up a string based on another string

result = '' # the string you're building starts empty
for char in text:
    if char != '<':
        result = result + char
        
    else:
        result = result[:-1]

print(result)

