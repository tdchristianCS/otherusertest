# 1. What does this code do?
# 2. Give each variable a logical name
# 3. Write good input/print strings

# The code asks for an even number.
# It then checks if it's even by seeing if there's a remainder
# after dividing it by 2. (No remainder = even number.)
# As long as it isn't even, it asks again.
# When you succeed, it prints a final statement.

number = int(input('Enter an even number: '))

while number % 2 != 0:
    print('Try again')
    number = int(input('Enter an even number'))

print('That will do')
