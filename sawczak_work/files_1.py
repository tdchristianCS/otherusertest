import os

# Change this if files don't end up where you want them or you get errors
BASE_PATH = 'sawczak_work/data'

def sign_up() -> None:
    username = input('Create a username: ').strip()
    password = input('Create a password: ').strip()

    # Open the database file in append mode (adding to it)
    # Write a new line with their username and password
    # separated by ::
    with open(f'{BASE_PATH}/database.txt', 'a') as database:
        line = username + '::' + password + '\n'
        database.write(line)

    print('You have signed up')


def log_in() -> str:
    # TODO
    pass


def run() -> None:

    # Make the base path folder (Python can't do this automatically)
    if not os.path.exists(BASE_PATH):
        os.mkdir(BASE_PATH)

    # Find out whether they want to sign up or log in
    choice = input('Enter [S]ign up or [L]og in: ').upper().strip()

    if choice.startswith('S'):
        sign_up()

    elif choice.startswith('L'):
        logged_in_username = log_in()
        # More will happen here


# The only part that executes directly
run()
