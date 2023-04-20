letters = 'ABC'
numbers = '123'

### non-nested
##
##for letter in letters:
##    print(letter)
##
##for number in numbers:
##    print(number)
##
### 6 total (adding total quantity)
##
### nested
##
##for letter in letters:
##    for number in numbers:
##        print(letter + number)
##
### 9 total (multiplying total quantity)
##
### even more nesting
##
##puncts = ':.!'
##
##for letter in letters:
##    for number in numbers:
##        for punct in puncts:
##            print(letter + number + punct)

# 27 total (multiplying 3 x 3 x 3)

# number seats in a theatre

##rows = 'ABCDEFG' # 7 rows
##cols = '123456789' # 9 cols (seats per row)
##
##for row in rows:
##    for col in cols:
##        print(row + col)

# as a range -- just specify a number

rows = 26
cols = 16

for r in range(rows):
    for c in range(cols):
        row = chr(65 + r) # 65 = A
        col = str(c + 1)
        print(row + col)

        

