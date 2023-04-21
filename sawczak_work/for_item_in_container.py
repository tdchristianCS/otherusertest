grades = [77, 81, 92, 70, 10, 100, 15, 65, 83]

# suppose that I want to add 5 to every grade
higher_grades = []
# higher_grades.append(grades[0] + 5)
# higher_grades.append(grades[1] + 5)
# higher_grades.append(grades[2] + 5)
# wait... we don't want to have to do this for every item...

for grade in grades:
    higher_grades.append(grade + 5)

print(grades)
print(higher_grades)

for grade in higher_grades:
    print(grade)
