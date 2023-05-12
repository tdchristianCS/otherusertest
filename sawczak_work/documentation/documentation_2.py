# Documentation practice 2

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

def mist_tree(a, b):
    c = []
    for d in a:
        if d not in b:
            c.append(d)
    return c

# Testing area
a = None # Change once you understand the required type
b = None # Change once you understand the required type
print(mist_tree(a, b))
