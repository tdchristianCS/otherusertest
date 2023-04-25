# # Counting vowels in a string

# vowels = 'aeiou'
# n_vowels = 0

# name = input('Enter your name: ')
# for char in name:                   # With strings, we call the loop variable 'c' or 'char' for 'character'
#     if char.lower() in vowels:
#         n_vowels = n_vowels + 1

# print(f'You have {n_vowels} vowels in your name.')

# =============================================================================

# # Counting integers in a list

# student_grades = [80, 50, 75, 92, 36, 67, 88, 90, 68, 73, 77]
# n_to_contact = 0

# for grade in student_grades:
#     if grade < 70:
#         n_to_contact = n_to_contact + 1

# print(f'{n_to_contact} students are at less than 70% and should be contacted')

# =============================================================================

# chess_pieces_living = ['Black Pawn', 'Black Pawn', 'Black King', 'White King', 'White Queen', 'Black Knight', 'White Rook']
# n_black = 0
# n_white = 0

# for piece in chess_pieces_living:
#     if 'Black' in piece:
#         n_black += 1
#     if 'White' in piece:
#         n_white += 1

# print(f'{n_black} black pieces alive')
# print(f'{n_white} white pieces alive')

# =============================================================================

# TASK
# User enters a password
# You have to count to make sure they have used...
# at least 1 number
# at least 1 symbol
# at least 1 uppercase letter
# at least 1 lowercase letter
# at least 8 characters total

# password = input('Enter password: ')

# numbers = '1234567890'
# symbols = '!@#$%^&*()'
# uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lowercase = 'abcdefghijklmnopqrstuvwxyz'

# check_numbers = False
# check_symbols = False
# check_uppercase = False
# check_lowercase = False
# check_length = len(password) >= 8

# for char in password:
#     if char in numbers:
#         check_numbers = True
#     if char in uppercase:
#         check_uppercase = True
#     if char in lowercase:
#         check_lowercase = True
#     if char in symbols:
#         check_symbols = True

# if check_lowercase and check_length and check_numbers and check_symbols and check_uppercase:
#     print('Valid!')
# else:
#     print('Invalid!')

# =============================================================================

# Same but cleaner using Python string methods

password = input('Enter password: ')

check_numbers = False
check_symbols = False
check_uppercase = False
check_lowercase = False
check_length = len(password) >= 8

for char in password:
    if char.isdigit():
        check_numbers = True
    elif char.isupper():
        check_uppercase = True
    elif char.islower():
        check_lowercase = True
    else:
        check_symbols = True

print(f'lowercase: {check_lowercase}')
print(f'uppercase: {check_uppercase}')
print(f'symbols: {check_symbols}')
print(f'numbers: {check_numbers}')

if check_lowercase and check_length and check_numbers and check_symbols and check_uppercase:
    print('Valid!')
else:
    print('Invalid!')
