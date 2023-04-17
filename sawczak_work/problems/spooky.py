# write a program that..

# takes a number from the user

# and prints the word 'spooky'
# with the number of 'o's equal to the # they gave you

# e.g. if they were to type 5
# your program would print
# spoooooky


# -- hint: you can multiply strings by numbers


n_os = int(input('Type in a number: '))
word = 'sp' + ('o' * n_os) + 'ky'
print(word)