password = input()
result = 'Valid' # flag

if len(password) < 8 or len(password) > 12:
    result = 'Invalid'

n_digits = 0
n_uppers = 0
n_lowers = 0

for c in password:
    if c.islower():
        n_lowers += 1
    elif c.isupper():
        n_uppers += 1
    elif c.isdigit():
        n_digits += 1

if n_lowers < 3 or n_uppers < 2 or n_digits < 1:
    result = 'Invalid'

print(result)