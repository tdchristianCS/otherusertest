# a second kind of for loop!
# for element in container

s = 'Hello' # a string is a container of characters

# char will be set to each character of the string in turn
#for char in s:
#    print(char)

# we can combine loops and conditions
# use this to filter, e.g. here we are filtering vowels
s = 'Hello'
for char in s:
    if char in 'aeiou':
        print(char)

# Try the above, except count the number of vowels
# and print the total at the very end

#s = input('Enter some text: ')
n_vowels = 0
for char in s:
    if char in 'aeiou':
        n_vowels = n_vowels + 1 # increment the vowel counter
print('There are ' + str(n_vowels) + ' vowels in your text')

# tracing the above if the input were 'Hello'
# char = 'H'
# char is not in 'aeiou', so we move on, skipping the if block
# char = 'e'
# char IS in 'aeiou', so we add 1 to n_vowels
# char = 'l'
# char is not in 'aeiou', so we move on, skipping the if block
# char = 'l'
# char is not in 'aeiou', so we move on, skipping the if block
# char = 'o'
# char IS in 'aeiou', so we add 1 to n_vowels
# finally we print
# output: 'There are 2 vowels in your next'

# Try creating one that counts the number of capital letters

s = input('Enter some text: ')
n_capitals = 0
for char in s:
    if char.isupper():
    # if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # equivalent
    # if 65 <= ord(char) <= 90: # equivalent
        n_capitals = n_capitals + 1
print('There are ' + str(n_capitals) + ' capital letters')

# We can combine for i in range
# with the fact that strings have indices
s = 'Hello'
for i in range(5):
    print(s[i])

# Dynamic range based on string length
s = input('Enter some text: ')
for i in range(len(s)):
    print(s[i])

# We can also filter this way
# Try every other letter (every second letter)
s = input('Enter some text: ')
for i in range(len(s)):
    if i % 2: # modulus % yields the remainder after division
        print(s[i])

