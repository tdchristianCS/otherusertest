# two things as part of our job...

# we have to check all the years

# for each year, we have to check if it has distinct digits

def is_distinct(year: int) -> bool:
    """
    Return True iff all the digits in the given year
    are distinct, else return False.

    >>> is_distinct(1987)
    True
    >>> is_distinct(1988)
    False
    """
    year = str(year)
    for digit in year:
        if year.count(digit) > 1:
            return False
    return True

##year = int(input())
##found = False
##while not found:
##    year += 1
##    found = is_distinct(year)
##print(year)

import doctest
doctest.testmod()

