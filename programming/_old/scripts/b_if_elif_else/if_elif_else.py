# conditional means if/then

# if contains a 'gate' (a.k.a. a condition)
# that gate is either True or False
# if it's True, we do the thing
# if it's False, we don't do the thing

n = int(input('Enter a number: '))

if n > 10:
    print('Your number was greater than ten')
    print('You have such good taste in numbers')
    
print('Thank you for playing')

# Notice: an if statement ends with a colon :
# and is followed by an indented block
# whatever is indented is controlled by the if
# but when we return to the outer indentation, that happens no matter what

# We can also use else to give an alternative

n = int(input('Enter another number: '))

if n > 10:
    print('Your number was greater than ten')
else:
    print('Your number was less than or equal to ten')

# In fact, we can use elif (else if) to create further "pathways"

n = int(input('Enter yet another number: '))

if n > 10:
    print('Your number was greater than ten')
elif n < 10:
    print('Your number was less than ten')
else:
    print('The only remaining option is that your number was equal to ten')

# You can also use Boolean operators: not, and, or

age = input('Enter your age (numbers only): ')
if not age.isdigit():
    print('You were supposed to only enter numbers!')
    print('I give up.')
else:
    age = int(age) # since we know it's a number, it's safe to cast to integer
    print("If you were three years younger you'd be " + str(age - 3))
