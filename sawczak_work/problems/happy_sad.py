# write a program that does sentiment analysis
# on a sentence that the user gives you

# tells you whether a social post is positive, negative, or neutral

# if the sentence contains more :) than :(, it's positive
# if the sentence contains more :( than :), it's negative
# if the sentence contains an equal number, it's neutral

# ====

# e.g. if they enter ':)'
# your program outputs 'positive'
# if they enter ':(:(:):)'
# your program outputs 'neutral'
# if they enter 'i am going to fly'
# your program outputs 'neutral'

# ====

sentence = input('Enter post here: ')

n_happy_faces = sentence.count(':)')
n_sad_faces = sentence.count(':(')

if n_happy_faces > n_sad_faces:
    print('positive')
elif n_happy_faces < n_sad_faces:
    print('negative')
elif n_happy_faces == n_sad_faces:
    print('neutral')
