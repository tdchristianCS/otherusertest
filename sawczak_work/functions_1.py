# DEFINE
def sqrt(n: int) -> float:    
    return n ** (1/2)

# DEFINE
def factorial(n: int) -> int:

    if n < 0:
        return 0
    
    else:
        product = 1

        for multiplier in range(1, n + 1):
            product = product * multiplier
        
        return product

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

import doctest
doctest.testmod()

# INVOKE
# for i in range(26):
#     square_root = sqrt(i)
#     print(f'sqtr of {i}: {square_root}')




