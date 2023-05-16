import random

PATH_1 = 'sawczak_work/data/test1.txt'
PATH_2 = 'sawczak_work/data/test2.txt'

# write mode: replaces the entire file
with open(PATH_1, 'w') as f:
    line = str(random.randint(1, 100)) + '\n'
    f.write(line)

# append mode: adds to the existing file
with open(PATH_2, 'a') as f:
    line = str(random.randint(1, 100)) + '\n'
    f.write(line)
