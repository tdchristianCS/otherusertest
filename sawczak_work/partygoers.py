cant_come_to_party = 'carl'
names = input('Enter partygoers separated by spaces: ').lower().split(' ')

if cant_come_to_party in names:
    print(f'{cant_come_to_party} is not allowed!!! Party is off')
else:
    print('All is well')