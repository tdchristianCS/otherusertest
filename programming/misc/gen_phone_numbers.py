import random
from typing import Iterator

def flip() -> bool:
    """Randomly return True or False with equal probability."""
    return bool(random.randint(0, 1))

def block(n: int) -> str:
    """Return a block of digits from 0-9 of length n."""
    numbers = [str(random.randint(0, 9)) for _ in range(n)]
    return ''.join(numbers)

def sep() -> str:
    """Return a random separator, or none at all."""
    return random.choice(['.', ' ', '-', ''])

def gen_phone_numbers(n: int) -> Iterator[str]:
    """Generate and yield n phone numbers."""
    for _ in range(n):
        yield(gen_phone_number())

def gen_phone_number() -> list[str]:
    """Return a random phone number."""
    
    # country code
    number = ''
    if flip():
        number += '+'
        if flip():
            number += '1'
        if flip():
            number += ' '

    # area code
    ac = block(3)
    if flip():
        number += f'({ac})'
    else:
        number += ac

    # rest
    number += sep()
    number += block(3)
    number += sep()
    number += block(4)
    return number

for number in gen_phone_numbers(50):
    print(number)
