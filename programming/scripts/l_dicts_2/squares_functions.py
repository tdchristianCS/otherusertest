# Consider this dictionary representation of a standard math function, square

# f(x) = x^2

SQUARES = {
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}


# Reminder: a mathematical function takes an input
# and gives a definite output (no randomness)

# Domain: allowed inputs (x values)
# Range: possible outputs (y values)

# domain of the square function is real numbers
# range of the square function is real numbers >= 0

# Each value in the domain yields one
# and only one value in the range

# Nevertheless... each value in the range
# does NOT need to have only one value in
# the domain

# Now let's observe a second function, the inverse: square root

# f(x) = sqrt(x)

SQUARE_ROOTS = {
    25: 5,
    16: 4,
    9: 3,
    4: 2,
    1: 1
}

# because it's the inverse of square, the domain and range are flipped
# domain of the square root function is real numbers >= 0
# range of the square root function is real numbers

# Now for the problem!
# What if a value has multiple keys in the original dictionary?

# Here's an extended version of the squares dictionary with a few more keys

SQUARES = {
    -5: 25,
    -4: 16,
    -3: 9,
    -2: 4,
    -1: 1,
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

# When inverted, we would run into the problem that 25 can't point to 5 and -5
# simultaneously. But what we CAN do is make it point to a list.

# The inverted dictionary should look like this

SQUARE_ROOTS = {
    25: [5, -5],
    16: [4, -4],
    9: [3, -3],
    4: [2, -2],
    1: [1, -1]
}

# Now let's write code to invert a dictionary;
# i.e., to generate someting like SQUARE_ROOTS from something like SQUARES

def invert(d: dict) -> dict:
    """
    Return the given dictionary inverted. Each {value: key} pair
    should become a {key: [value]} pair, i.e. a key points to a list
    of values that were the original keys. If more than one key points
    to the same value, that  list would look like {value: [key, key, key...]}

    Note: the order of the value list is not important.

    >>> invert({'A': 1, 'B': 2})
    {1: ['A'], 2: ['B']}
    >>> invert({'C': 3, 'D': 4, 'E': 3})
    {3: ['C', 'E'], 4: ['D']}
    """

    
    result = {}
    for item in d.items(): # items are [key, value] pairs
        orig_key = item[0]
        orig_value = item[1]
        
        # if it's the first time, initialize a 1-item list
        if orig_value not in result:
            result[orig_value] = [orig_key]

        # if it's not the first time, append it to the list
        # that we made when we saw it the first time
        else:
            result[orig_value].append(orig_key)

        # print(result) # uncomment to see how the dictionary grows
        
    return result


