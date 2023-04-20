def exponentiate(m: int, n: int) -> int:
    """
    Return m raised to the nth power.
    n is a positive integer.
    """
    result = 1
    for i in range(n):
        result = result * m
    return result

# opposite...
def un_exponentiate(m: int, n: int) -> float:
    """
    Return m divided by itself n times.
    n is a positive integer.
    """
    result = m
    for i in range(n):
        result = result / m
    return result

# negative exponents
def negative_exponentiate(m: int, n: int) -> float:
    """
    Return m raised to negative n.
    n is a positive integer.
    """
    result = 1
    for i in range(n):
        result = result * (1 / m)
    return result

# now... make a function exponentiate2
# that takes m and n
# if n is positive, do exponentiation (9 x 9 x 9...)
# and if n is negative, does the inverse exponentiation (1/9 x 1/9 x 1/9 ...)

# both conditionally
def exponentiate2(m: int, n: int) -> float: # int or float??
    """
    Return m raised to n.
    n is an integer.
    """
    if n >= 0:
        return exponentiate(m, n)
    else:
        return negative_exponentiate(m, -n)
    
