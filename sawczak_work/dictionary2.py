cipher = {
    'a':     'z',
    'b':     'y',
    'c':     'x',
    'd':     'w',
    'e':     'v',
    'f':     'u',
    'g':     't',
    'h':     's',
    'i':     'r',
    'j':     'q',
    'k':     'p',
    'l':     'o',
    'm':     'n',
    'n':     'm',
    'o':     'l',
    'p':     'k',
    'q':     'j',
    'r':     'i',
    's':     'h',
    't':     'g',
    'u':     'f',
    'v':     'e',
    'w':     'd',
    'x':     'c',
    'y':     'b',
    'z':     'a',
}

decipher = {
    'z':     'a',
    'y':     'b',
    'x':     'c',
    'w':     'd',
    'v':     'e',
    'u':     'f',
    't':     'g',
    's':     'h',
    'r':     'i',
    'q':     'j',
    'p':     'k',
    'o':     'l',
    'n':     'm',
    'm':     'n',
    'l':     'o',
    'k':     'p',
    'j':     'q',
    'i':     'r',
    'h':     's',
    'g':     't',
    'f':     'u',
    'e':     'v',
    'd':     'w',
    'c':     'x',
    'b':     'y',
    'a':     'z',
}

def encode(message):
    coded = ''

    for char in message:
        if char.lower() in cipher:
            coded += cipher[char.lower()]
        else:
            coded += char
    
    return coded

def decode(message):
    decoded = ''

    for char in message:
        if char.lower() in decipher:
            decoded += decipher[char.lower()]
        else:
            decoded += char
    
    return decoded

while True:
    choice = int(input('Enter (1) encode / (2) decode: '))
    msg = input('Enter message: ')

    if choice == 1:
        print(encode(msg))
    else:
        print(decode(msg))
