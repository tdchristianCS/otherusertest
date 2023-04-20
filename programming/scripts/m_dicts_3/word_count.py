from typing import Dict, List

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

def most_frequent_from_counts(counts: dict) -> List[str]:
    """
    Given a dictionary, output the most frequent values.

    >>> most_frequent({'Anthony': 'Black'})
    'Black'
    >>> most_frequent({'Anthony': 'Black', 'Calum': 'Brown', 'Jacob': 'Brown'})
    'Brown'
    """

    # inverted counts looks like {4: ['Black', 'Brown']}
    inverted_counts = invert(counts)
    highest_key = max(inverted_counts) # e.g. 5

    return inverted_counts[highest_key]


def sanitize(word: str) -> str:
    """
    Return the given word, sanitized.

    >>> sanitize('Hello')
    'hello'
    >>> sanitize('dog.')
    'dog'
    """

    word = word.lower()
    word = word.strip('.?!,:;@#$%^&*(){}[]/')
    return word    
    

def word_counts(text: str) -> Dict[str, int]:
    """
    Given a text, return a dictionary mapping words to the number of times
    each word appears.

    Note: ignore case & punctuation (but leave this part for later. just do
    your test cases without worrying about it)

    >>> word_counts('hi bob')
    {'hi': 1, 'bob': 1}
    >>> word_counts('ha ha ha u r funny u cat')
    {'ha': 3, 'u': 2, 'funny': 1, 'r': 1, 'cat': 1}
    """

    counts = {}
    words = text.split()
    for word in words:

        # sanitize the word
        word = sanitize(word)
        
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    return counts



user_input = input('Enter some text: ')
words = word_counts(user_input)
print(words)

print(most_frequent_from_counts(words))
