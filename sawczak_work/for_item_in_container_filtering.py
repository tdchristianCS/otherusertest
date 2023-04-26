# Filtering 1

students = ['Julia', 'Hogan', 'Colin', 'Christian', 'Fenchyl', 'William', 'Adrian', 'Josh Min', 'Josh Carone', 'Jack', 'Jaewook', 'Daniel', 'Stephen', 'Zequan']
eligible = ['Hogan', 'Adrian', 'Jack', 'Daniel', 'Josh Min']

# Filter down to the ineligible
ineligible = []

for student in students:
    if student not in eligible:
        ineligible.append(student)

print('Ineligible students:')
print(ineligible)

# =============================================================================

# Filtering 2
# Sanitize text by removing anything that is not an English letter or a space

name = input('Enter name: ')
sanitized = ''

for char in name:
    if char.isalpha() or char.isspace():
        sanitized = sanitized + char

print(f'Sanitized name: {sanitized}')

# =============================================================================

# Filtering 3
# Adapt the above so only vowels are sanitary

name = input('Enter name: ')
vowels = 'aeiou'
sanitized = ''

for char in name:
    if char.lower() in vowels:
        sanitized = sanitized + char

print(f'Sanitized name: {sanitized}')
