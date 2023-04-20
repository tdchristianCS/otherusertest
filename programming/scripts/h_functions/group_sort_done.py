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

    # reset cur_group to 0 (the first group) if we are past 2 (the third group)
    if cur_group == 3:
        cur_group = 0

    groups[cur_group].append(student)
    cur_group += 1 # go on to the next group

print(groups)

