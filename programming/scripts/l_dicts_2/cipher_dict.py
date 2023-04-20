CIPHER = {
    'a': 't',
    'b': 'h',
    'c': 'e',
    'd': 'q',
    'e': 'u',
    'f': 'i',
    'g': 'c',
    'h': 'k',
    'i': 'b',
    'j': 'r',
    'k': 'o',
    'l': 'w',
    'm': 'n',
    'n': 'f',
    'o': 'x',
    'p': 'j',
    'q': 'm',
    'r': 'p',
    's': 's',
    't': 'v',
    'u': 'l',
    'v': 'a',
    'w': 'z',
    'x': 'y',
    'y': 'd',
    'z': 'g'
}


def invert_dict(d: dict) -> dict:
    """
    Return the given dictionary inverted.
    That is, each key: value pair is now value: key.

    >>> invert({'a': 't', 'b': 'c'})
    {'c': 'b', 't': 'a'}
    """

    result = {}

    # HOW TO INVERT A DICTIONARY
    # loop through the items
    # each item is a list of two items [key, value]
    # i.e. item[0] is a key, and item[1] is a value
    # so we put them into a dict in the opposite order
    
    for item in d.items():
        orig_key = item[0] # e.g. a
        orig_value = item[1] # e.g. t
        result[orig_value] = orig_key # t = a
    return result
    

def encode(msg: str, cipher: dict) -> str:
    """
    Return the given message encoded."""

    result = ''
    for char in msg:

        if char.isalpha():        
            encoded = cipher[char.lower()]
            result += encoded
        else:
            result += char
            
    return result


def decode(msg: str, cipher: dict) -> str:

    de_cipher = invert_dict(cipher)
    result = encode(msg, de_cipher)
    return result    


mode = input('[E]ncode, [D]ecode, or [Q]uit: ').upper().strip()
while mode != 'Q':

    if mode == 'E':
        msg = input('\nEnter a message: ').strip()
        result = encode(msg, CIPHER)
        print(f'\nEncoded:\n{result}')
        
    elif mode == 'D':
        msg = input('\nEnter a message: ').strip()
        result = decode(msg, CIPHER)
        print(f'\nDecoded:\n{result}')
    
    mode = input('\n[E]ncode, [D]ecode, or [Q]uit: ').upper().strip()

