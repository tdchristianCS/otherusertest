secret_password = 'password123'
secret_login = 'coolguy67'

user_login = input('Enter your username: ').lower().strip()
user_password = input('Enter your password: ').strip()

if (user_login == secret_login) and (user_password == secret_password):
    print('You are logged in')
else:
    print('Username or password was wrong!!!')

print('Goodbye')
