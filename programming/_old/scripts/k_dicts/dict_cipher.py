encode_key = {
    'a': 'z',
    'b': 'c',
    'c': 'e',
    'd': 'f',
    'e': 'h',
    'f': 'o',
    'g': 'p',
    'h': 'w',
    'i': 'x',
    'j': 'y',
    'k': 'a',
    'l': 'd',
    'm': 'i',
    'n': 'm',
    'o': 'b',
    'p': 'n',
    'q': 'j',
    'r': 'g',
    's': 'v',
    't': 'u',
    'u': 't',
    'v': 'r',
    'w': 's',
    'x': 'k',
    'y': 'q',
    'z': 'l'
}

decode_key = {
}

def encode(msg: str) -> str:
    """
    Return the given message encoded.
    """

    result = ''

    msg = msg.lower()

    for char in msg:
        if not char.isalpha():
            result += char
            
        else:
            result += encode_key[char]

    return result

msg = input('Enter a sentence to encode: ')
print(encode(msg))
