# This code asks for two numbers. If the second number is 0, it prints a notice about this. Otherwise, it prints 1 over x over y (the inverse of x divided by y).

numerator = int(input('Enter a numerator: '))
denominator = int(input('Enter a denominator: '))
  
assert type(numerator) == int
assert type(denominator) == int

if denominator == 0:
  print('Denominator must not be 0')

elif numerator == 0:
  print('Numerator must not be 0')

else:  
  assert denominator != 0
  assert numerator != 0
  
  first_division = (numerator / denominator)
  assert first_division != 0
  
  inverse_quotient = 1 / first_division

  print(inverse_quotient)

# BONUS: The above code can still accidentally divide by zero. Explain how.
