x = 1
y = x + 1
z = x - 1

if x > y:
  x = x + 2
else:
  x = x + 3
if z < x:
  y = z
  if y >= z:
    x = z
  else:
    z = x

if z < x:
  print('z is small')
elif y < x:
  print('y is small')
else:
  print('x is small')
