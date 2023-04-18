# write a program that calculates the winning score
# for a basketball game

# there are six inputs in all.
# all are numbers.

# the first is team A's 3-point shots
# the second is team A's 2-point shots
# the third is team A's 1-point shot

# then the same for team B

# if team A's total score is greater than team B
# output Team A
# if team B's score total score is greater than team A
# output Team B
# if they tie
# output Tie

# =====

# example inputs and output

"""
Enter Team A's 3-pointers: 2
Enter Team A's 2-pointers: 5
Enter Team A's 1-pointers: 1
Enter Team B's 3-pointers: 3
Enter Team B's 2-pointers: 2
Enter Team B's 1-pointers: 2
Team A
"""

# team A scored 2 x 3, 5 x 2, 1 x 1 = 17
# team B scored 3 x 3, 2 x 2, 2 x 1 = 15
# so team A had the higher score
# so we printed Team A

# =====

# team a and b's 3, 2, and 1-pointers
a3 = int(input('Enter Team A\'s 3 pointers: '))
a2 = int(input('Enter Team A\'s 2 pointers: '))
a1 = int(input('Enter Team A\'s 1 pointers: '))

b3 = int(input('Enter Team B\'s 3 pointers: '))
b2 = int(input('Enter Team B\'s 2 pointers: '))
b1 = int(input('Enter Team B\'s 1 pointers: '))

a_total = (a3 * 3) + (a2 * 2) + (a1)
b_total = (b3 * 3) + (b2 * 2) + (b1)

if a_total > b_total:
    print('Team A wins')
elif b_total > a_total:
    print('Team B wins')
elif a_total == b_total:
    print('Tie')
