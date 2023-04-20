letter_to_presses = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    '.': '1',
    ',': '11',
    '?': '111',
    ' ': '0'
}

def T9ify(msg: str) -> str:
    """
    Return the given message where every letter is converted into
    the presses needed to type it on T9.

    >>> T9ify('hello')
    '443555555666'
    >>> T9ify('a')
    '2'
    """
    result = ''

    for char in msg:
        presses = letter_to_presses[char]
        result += presses
    return result

msg = input('Enter a sentence to T9ify: ')
print(T9ify(msg))
