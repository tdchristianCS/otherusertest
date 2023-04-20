# Write some code that implements ^ as CAPS LOCK
# It toggles whether you're typing in all caps

# So if CAPS LOCK is off and you hit ^, it's now on
# and if it's on and you hit ^, it's now off

# Take the user's input and output the result

# e.g.
# input:	'just ^kidding'
# output:	'just KIDDING'

# input:	'I ^know^, Mom'
# output:	'I KNOW, Mom'

# input:	'It's ^too^ easy'
# output:	'It's TOO easy'


sentence = input('Enter a sentence: ')
output = ''
caps_lock = False

for char in sentence:
    if char == '^':
        caps_lock = not caps_lock
        
    elif caps_lock:
        output += char.upper()
        
    else:
        output += char


print(output)






