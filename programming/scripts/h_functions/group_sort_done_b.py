import random

# from a list of students

students = input('Enter student names separated by spaces: ')
students = students.split()
random.shuffle(students) # this shuffles the students randomly

# place them randomly into 3 groups
# no student should appear in more than one group...
# every student must appear in some group....

# group size should be as even as possible
# but it may not end up even if n students % 3 != 0

groups = [[], [], []] # groups[0], groups[1], groups[2]

cur_group = 0
while len(students) > 0:
    student = students.pop()

    # by using % 3, we look for the remainder after dividing by 3
    # this self-resets to 0 every multiple of 3
    # (to see why: 0 % 3 = 0, 1 % 3 = 1, 2 % 3 = 2, 3 % 3 = 0, 4 % 3 = 1)

    groups[cur_group % 3].append(student)
    cur_group += 1 # go on to the next group

print(groups)

# modify so that it takes an arbitrary # of groups (> 0) from the user
# to prepare N empty groups, do this:

# to create N empty groups
groups = []
for i in range(N):
    groups.append([])
    
