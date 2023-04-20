

age = input('Enter your age (numbers only): ')
if not age.isdigit():
    print('I said numbers only!! start over')

    if age == 'paul':
        print('PAUL!!! I know it\'s you!!')
    else:
        print('at least you\'re not paul')
        
else:
    age = int(age)
