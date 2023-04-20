# take a user's input sentence
# output a censored version of it
# to do this, create a list of filter words
# that you will not accept in the sentence
# FOR SIMPLICITY, assume no punctuation
# however, it should handle uppercase/lowercase

# e.g.
# input: This assignment is such crap
# output: This assignment is such

censored = ['crap', 'crud', 'suck', 'sucks', 'dang', 'grandpa']
sentence = input('Enter a sentence, you filthy animal: ')
words = sentence.split()

new_sentence = []
for word in words:
    if word not in censored:
        new_sentence.append(word)

    # modification! Let's replace it with asterisks instead
    else:
        mask = word[0] + ('*' * (len(word) - 1))
        new_sentence.append(mask)
        
new_sentence = ' '.join(new_sentence)
print(new_sentence)
