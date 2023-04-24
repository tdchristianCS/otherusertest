# Counting vowels in a string

vowels = 'aeiou'
n_vowels = 0

name = input('Enter your name: ')
for char in name:                   # With strings, we call the loop variable 'c' or 'char' for 'character'
    if char.lower() in vowels:
        n_vowels = n_vowels + 1

print(f'You have {n_vowels} vowels in your name.')


# Counting integers in a list

student_grades = [80, 50, 75, 92, 36, 67, 88, 90, 68, 73, 77]
n_to_contact = 0

for grade in student_grades:
    if grade < 70:
        n_to_contact = n_to_contact + 1

print(f'{n_to_contact} students are at less than 70% and should be contacted')
