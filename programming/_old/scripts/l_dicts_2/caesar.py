def caesar_cipher(msg: str, n: int) -> str:
    """
    Return the given message shifted by the given number
    of letters.
    """

    result = ''

    msg = msg.lower()

    for char in msg:
        if not char.isalpha():
            result += char
            
        else:        
            new_ord = ord(char) + n
            new_ord = (new_ord - 97) % 26 + 97
            result += chr(new_ord)

    return result

def encode(msg: str, n: int) -> str:
    return caesar_cipher(msg, n)

def decode(msg: str, n: int) -> str:
    return caesar_cipher(msg, -n)

mode = input('[E]ncode, [D]ecode, or [Q]uit: ').upper().strip()
while mode != 'Q':
    msg = input('\nEnter a message: ').strip()
    n = int(input('Enter shift key: ').strip())
    
    if mode == 'E':
        print(f'\nEncoded:\n{encode(msg, n)}')
    elif mode == 'D':
        print(f'\nDecoded:\n{decode(msg, n)}')
    
    mode = input('\n[E]ncode, [D]ecode, or [Q]uit: ').upper().strip()



