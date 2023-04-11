import math

# ask for the number of students in the class and slices per student
n_students = int(input('How many students are in the class? '))
n_slices_per_student = int(input('How many slices should each student receive? '))

# a pizza has 8 slices
n_slices_per_pizza = 8

# calculate the total number of slices
n_total_slices = n_students * n_slices_per_student

# print the total number of pizzas needed to order
# (extra credit: round that number up since you can't order half a pizza)
n_pizzas = n_total_slices / n_slices_per_pizza
print(math.ceil(n_pizzas))
