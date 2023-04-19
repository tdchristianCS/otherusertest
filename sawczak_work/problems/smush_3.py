# write a program that works like smush_names.py,
# except it takes 3 names and combines them in thirds.

# ====

# Here is a sample set of inputs and output

"""
Enter a name: Robert
Enter a name: Paul
Enter a name: Yiwen
Roawen
"""

# ====

name_1 = input('Enter a name: ').strip()
name_2 = input('Enter a name: ').strip()
name_3 = input('Enter a name: ').strip()

first_third_1 = len(name_1) // 3
first_third_2 = len(name_2) // 3
first_third_3 = len(name_3) // 3

last_third_1 = (len(name_1) // 3) * 2
last_third_2 = (len(name_2) // 3) * 2
last_third_3 = (len(name_3) // 3) * 2

smush = name_1[:first_third_1] + name_2[first_third_2:last_third_2] + name_3[last_third_3:]
print(smush)
