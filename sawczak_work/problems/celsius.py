# write a program that takes a number in degrees Fahrenheit
# and outputs the equivalent in degrees Celsius.

# ====

# e.g. if they enter 32
# your program prints 0.0
# if they enter -40
# your program prints -40.0

# ====

temp = float(input('Enter your temp in Fahrenheit: '))
temp = (temp - 32) * 5/9
print(temp)
