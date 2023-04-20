from typing import Dict, List # just for annotations

GENDERS = {
    'Anthony': 'Male',
    'Calum': 'Male',
    'Karim': 'Male',
    'Matthew': 'Male',
    'Daniel': 'Male',
    'Josh E': 'Male',
    'Josh C': 'Male',
    'Nathan': 'Male',
    'Joseph': 'Male',
    'Jack': 'Male',
    'Lazar': 'Male',
    'Sharon': 'Female',
    'Meagan': 'Female',
    'Joyce': 'Female',
    'Risa': 'Female',
    'Mickey': 'Male',
    'Jacob': 'Male'
}

HAIR_COLOURS = {
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

def most_frequent_from_dict(d: Dict[str, str]) -> List[str]:
    """
    Given a dictionary, output the most frequent values.

    >>> most_frequent({'Anthony': 'Black'})
    'Black'
    >>> most_frequent({'Anthony': 'Black', 'Calum': 'Brown', 'Jacob': 'Brown'})
    'Brown'
    """

    counts = {} # {'Black': 1, 'Brown': 2}
    for value in d.values():
        if value not in counts:
            counts[value] = 1
        else:
            counts[value] += 1

    # inverted counts looks like {4: ['Black', 'Brown']}
    inverted_counts = invert(counts)
    highest_key = max(inverted_counts) # e.g. 5

    return inverted_counts[highest_key]

def most_frequent_from_list(L: list) -> list:
    """
    Given a list, output the most frequent values.

    >>> most_frequent_from_list([1, 3, 4, 5, 5])
    [5]
    >>> most_frequent_from_list([1, 1, 3, 3, 4])
    [1, 3]
    """

    counts = {}
    for number in L:
        number = int(number)
        
        if number not in counts:
            counts[number] = 1
        else:
            counts[number] += 1

    inverted_counts = invert(counts)
    highest_key = max(inverted_counts)
    return inverted_counts[highest_key]

    
# Take as input from the user a single line
# containing values separated by spaces
# e.g. 9 8 9 4 3 0 1 -5 3
# print a list of modes in the set
# e.g. [9, 3]

numbers = input('Enter numbers: ')
numbers = numbers.split()
print(most_frequent_from_list(numbers))




    
