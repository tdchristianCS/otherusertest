import random

# from a list of students

students = input('Enter student names separated by spaces: ')
students = students.split()
random.shuffle(students) # this shuffles the students randomly

n_groups = int(input('Enter number of groups: '))

# place them randomly into 3 groups
# no student should appear in more than one group...
# every student must appear in some group....

# group size should be as even as possible
# but it may not end up even if n students % 3 != 0

# to create N empty groups
groups = []
for i in range(n_groups):
    groups.append([])

cur_group = 0
while len(students) > 0:
    student = students.pop()

    # by using % 3, we look for the remainder after dividing by 3
    # this self-resets to 0 every multiple of 3
    # (to see why: 0 % 3 = 0, 1 % 3 = 1, 2 % 3 = 2, 3 % 3 = 0, 4 % 3 = 1)

    groups[cur_group % n_groups].append(student)
    cur_group += 1 # go on to the next group

# let's do this more attractively
# print(groups)

# Attractive nested list printing: nested for loops
print()
for (i, group) in enumerate(groups): # this gives us an index for our loop
    print(f'GROUP {i + 1}') # group heading
    for student in group:
        print(f'     {student}') # indent student names
    print() # blank line after each group


# Version that takes a desired # of spaces
# Attractive nested list printing: nested for loops
n_spaces = int(input('Enter desired indentation: '))
print()
for (i, group) in enumerate(groups): # this gives us an index for our loop
    print(f'GROUP {i + 1}') # group heading
    for student in group:
        print(f'{" " * n_spaces}{student}') # indent student names
    print() # blank line after each group
    
