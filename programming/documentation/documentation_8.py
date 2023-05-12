# Documentation practice 8

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

def mister_e(a, b):
    c = len(a) // 2
    d = len(b) // 2
    e = a[:c] + b[d:]
    return e.title()

# Testing area
a = None # Change once you understand the required type
b = None # Change once you understand the required type
print(mister_e(a, b))
