# FUNCTIONS

# Start with a signature
def do_a_thing():
    # then the body
    print('Hello!')

# now I can call that function whenever I like
do_a_thing()

# while loop -- call a function based on user input
choice = input('Do you want to do a thing? Y/N: ').strip()
while choice:
    if choice.upper() == 'Y':
        do_a_thing()
    choice = input('Do you want to do a thing? Y/N: ').strip()
print('Thanks for stopping by!')
