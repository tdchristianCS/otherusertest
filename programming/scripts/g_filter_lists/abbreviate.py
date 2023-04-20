# take a user's input sentence
# abbreviate it by chopping each word in half

sentence = input('Enter a sentence: ')
words = sentence.split()

new_sentence = []
for word in words:
    length = len(word)
    abbrev = word[:round(length / 2)]
    new_sentence.append(abbrev)
new_sentence = ' '.join(new_sentence)
print(new_sentence)
