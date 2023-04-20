# conditional means if/then

# if contains a 'gate' (a.k.a. a condition)
# that gate is either True or False
# if it's True, we do the thing
# if it's False, we don't do the thing
##n = int(input('Enter a number: '))
##if n > 10:
##    print('Your number was greater than ten')
##    print('You are a genius')
##    print('You have such good taste in numbers')
##else:
##    print('You number was less than or equal to ten')
##print('Thank you for playing')



gender = input('Enter M or F for gender: ')
if gender == 'M' or gender == 'ACAB' or gender == 'X':
    expected_weight = 165
elif gender == 'F':
    expected_weight = 150
else:
    print('I did not understand.')
    
weight = int(input('What is your weight in pounds: '))

life_expectancy = 90 - (weight - expected_weight)
print(life_expectancy)

age = input('Enter your age (numbers only)')
if not age.isdigit():
    print('I said numbers only!!!')
else:
    age = int(age)

