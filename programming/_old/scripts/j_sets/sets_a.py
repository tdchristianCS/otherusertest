# set of real numbers
# this is a set of infinite size
# 0.01   99.9   15651.78

# we can also make sets of finite size
# set of integers greater than 1 and less than 10
# 2 3 4 5 6 7 8 9

# isn't this just a list?
# not quite

# LIST: each index maps to a value; stores order of values
# SET: defined by membership, not index; order of values is random

# Sets do not have duplicates
L = [1, 7, 5, 7, 4, 2, 4, 1] # valid
set(L) # {1, 7, 5, 4, 2}

# How could you use this to check distinct years more easily? Example:
def is_distinct(year: str) -> bool:
    """
    Return True iff all digits in the given year are distinct.
    """

    return len(year) == len(set(year)) # if digits repeat, set will be shorter
