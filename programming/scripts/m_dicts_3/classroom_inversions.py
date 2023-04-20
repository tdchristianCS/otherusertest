# YOUR TASK IS...

# Create a dictionary of people in the class (p.s. I've attached a starter)
# Choose any quality for them, and map their name to that quality

NAMES = {
    'Anthony': 'Black',
    'Calum': 'Brown',
    'Karim': 'Dark brown',
    'Matthew': 'Blond',
    'Daniel': 'Brown',
    'Josh E': 'Dark brown',
    'Josh C': 'Black',
    'Nathan': 'Dark brown',
    'Joseph': 'Black',
    'Jack': 'Blond',
    'Lazar': 'Brown',
    'Sharon': 'Dark brown',
    'Meagan': 'Dark blond',
    'Joyce': 'Black',
    'Risa': 'Blond',
    'Mickey': 'Dark brown',
    'Jacob': 'Brown'
}


# Then, adapt our code to invert this dictionary
# So that we have a new dictionary of qualities to names

def bad_invert(d: dict) -> dict:
    result = {}
    for item in d.items(): # items are [key, value] pairs
        orig_key = item[0]
        orig_value = item[1]
        result[orig_value] = orig_key

        # print(result) # uncomment to see how the dictionary grows
        
    return result

# Make this inversion a function
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

