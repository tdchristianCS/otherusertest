text = input('Enter some text: ')

n_vowels = 0 # Counter for vowels
for char in text:
    if char.upper() in 'AEIOU': # force uppercase so we get both cases
        n_vowels += 1

# format strings allow you to insert variables more elegantly
# f'text {variable name} text' <- note those are curly braces {}

print(f'You have {n_vowels} vowels in your text.')

n_words = 0
for char in text:
    if char in ' ':
        n_words += 1
n_words += 1
print(f'You have {n_words} words in your text.')

n_lower = 0
for char in text:
    if char in 'abcdefghijklmnopqrstuvwxyz':
        n_lower += 1
print(f'You have {n_lower} lowercase letters in your text.')

n_punct = 0
for char in text:
    if char in ':;.,/?!@#$%^&*()[]{}\\"\'':
        n_punct += 1
print(f'You have {n_punct} pieces of punctuation in your text.')

# Sentences is slightly more complicated! We want to avoid
# ... being three sentences
# So we keep track of the last character we saw, and make sure
# we only add a sentence if it's not two or more in a row.
n_sentences = 0
last_seen = ''
for char in text:
    if char in '.?!':
        if last_seen not in '.?!':
            n_sentences += 1
    last_seen = char
print(f'You have {n_sentences} sentences in your text.')
