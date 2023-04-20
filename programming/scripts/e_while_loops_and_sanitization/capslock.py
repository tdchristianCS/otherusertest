# Make a caps lock function
# The character for caps lock will be ^

# caps lock key toggles caps lock on or off (it starts off)
# while caps lock is on, all characters typed become uppercase

text = input('Enter some text. ^ is caps lock: ')
result = ''

caps_lock = False # whether caps lock is currently on or not

for char in text:
    # Choice 1: is it a caret or not?
    
    if char == '^':

        # If caps lock is on, turn it off
        # If it's off, turn it on
        
        if caps_lock:
            caps_lock = False
        else:
            caps_lock = True
            
    else:

        # If caps lock is on and we hit a letter, capitalize it
        # If caps lock is off and we hit a letter, just add it
        
        if caps_lock:
            # add uppercase char to result
            result = result + char.upper()
        else:
            # add char as it is to result
            result = result + char

print(result)




# test cases

# in:   jacob smith
# out:  jacob smith

# in:   j^acob smith
# out:  jACOB SMITH

# in:   j^oyc^e min
# out:  jOYCe min

# in:   Jo^yce^ min
# out:  JoYCE min

