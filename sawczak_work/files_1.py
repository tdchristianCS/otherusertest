import os

# Change this if files don't end up where you want them or you get errors
BASE_PATH = 'sawczak_work/data'

def validate_password(password: str) -> bool:
    """
    Return True iff the given password is valid,
    and False iff the given password is invalid.

    A valid password is defined as having 12+ characters.
    """

    return len(password) >= 12

def sign_up() -> None:
    username = input('Create a username: ').strip()

    password = input('Create a password: ').strip()
    while not validate_password(password):
        print('Password must have 12+ characters')
        password = input('Create a password: ').strip()

    # Open the database file in append mode (adding to it)
    # Write a new line with their username and password
    # separated by ::
    with open(f'{BASE_PATH}/database.txt', 'a') as database:
        line = username + '::' + password + '\n'
        database.write(line)

    print('You have signed up')


def log_in() -> str:

    # It's OK to use the infinite 'while True' loop because the use of return
    # will instantly end the function when they successfully log in
    while True:
        username = input('Enter your username: ').strip()
        password = input('Enter your password: ').strip()
        
        with open(f'{BASE_PATH}/database.txt', 'r') as database:
            # This method is for reading an entire file as a single string
            # content = database.read()

            # This method is for reading a file line by line
            for line in database.readlines():
                line = line.strip() # removes the \n newline character
                maybe_username, maybe_password = line.split('::')

                if (username == maybe_username) and (password == maybe_password):
                    print(f'Logging in {username}')
                    return username
            
            # If they get here, no lines matched
            print('That combination could not be found')

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
