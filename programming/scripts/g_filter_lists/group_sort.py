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

while len(students) > 0:
    student = students.pop()

print(groups)

