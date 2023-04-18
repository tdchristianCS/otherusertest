name_1 = input('Enter a name: ')
name_2 = input('Enter a name: ')

halfway_1 = len(name_1) // 2
halfway_2 = len(name_2) // 2

smush_1 = name_1[:halfway_1] + name_2[halfway_2:]
print(f'Your child\'s name option 1 is {smush_1}')

smush_2 = name_2[:halfway_2] + name_1[halfway_1:]
print(f'Your child\'s name option 2 is {smush_2}')
