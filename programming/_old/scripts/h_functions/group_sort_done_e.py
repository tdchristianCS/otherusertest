import random
from typing import List

def get_student_names() -> List[str]:
    """
    Ask the user for student names, and return a list of said names
    in random order.
    """
    students = input('Enter student names separated by spaces: ')
    students = students.split()
    random.shuffle(students) # this shuffles the students randomly
    return students

def make_empty_groups(n_groups: int) -> List[List]:
    """
    Return a list of n_groups empty lists.
    """
    groups = []
    for i in range(n_groups):
        groups.append([])
    return groups

def fill_groups(students: List[str], groups: List[List]) -> None:
    """
    Distribute the given students into the given groups randomly
    and as evenly as possible.
    Note: changes the lists in place.
    """
    cur_group = 0
    while len(students) > 0:
        student = students.pop()

        groups[cur_group % n_groups].append(student)
        cur_group += 1

# printing functions usually don't return anything
# they just print to the shell
def print_groups(groups: List[List[str]]):
    """
    Print the given groups in an attractive manner,
    with groups headings and indented group members.
    """
    print()
    for (i, group) in enumerate(groups): # this gives us an index for our loop
        print(f'GROUP {i + 1}') # group heading
        for student in group:
            print(f'     {student}') # indent student names
        print() # blank line after each group


students = get_student_names()
n_groups = int(input('Enter number of groups: '))
groups = make_empty_groups(n_groups)
fill_groups(students, groups)
print_groups(groups)

