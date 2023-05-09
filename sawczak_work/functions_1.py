# DEFINE
def sqrt(n: int) -> float:    
    return n ** (1/2)

# INVOKE
for i in range(1, 10):
    square_root = sqrt(i)
    print(f'sqtr of {i}: {square_root}')

# DEFINE
def factorial(n: int) -> int:

    if n < 0:
        return 0
    
    else:
        product = 1

        for multiplier in range(1, n + 1):
            product = product * multiplier
        
        return product
    
# INVOKE
for i in range(1, 10):
    square_root = factorial(i)
    print(f'factorial of {i}: {factorial}')

# DEFINE
# In this one, the """ ... """ thing is called a docstring
# You write an example of how to use it and what you would expect to happen
def remove_all(L: list, thing_to_remove: object) -> None:
    """
    Remove every copy of thing_to_remove from L.

    >>> test_list = [1, 2, 3, 4]
    >>> remove_all(test_list, 3)
    >>> print(test_list)
    [1, 2, 4]
    """

    while thing_to_remove in L:
        L.remove(thing_to_remove)
    
    return

# TEST
# When you have the docstring above, you can use doctest to run your tests
# If you see nothing, it means your function passed the tests
# Otherwise it will tell you what went wrong
import doctest
doctest.testmod()

# INVOKE
test_list = [3, 3, 3, 3, 4]
remove_all(test_list)
print(test_list)

