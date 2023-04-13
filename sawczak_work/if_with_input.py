smokes = input('Do you smoke (Y/N): ').lower().strip()
smoking_factor = 0

if smokes == 'y':
    print('Quit tomorrow!')
    smoking_factor = -10

elif smokes == 'n':
    print('Good. Keep it that way')

else:
    print('Invalid input')

# Update death clock with 3 yes/no questions
# Extra credit: Ask a question ONLY IF they said yes to another
# e.g. you ask their gender, and if they enter 'F', then ask # of children
