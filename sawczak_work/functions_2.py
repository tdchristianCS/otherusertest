import math
import time
import os

def rng() -> int:
    rn = 1
    n1 = get_n1()
    n2 = get_n2()

    rn *= (n1 * math.pi)

    # turn that into a string, and take the part after the period
    s_rn = str(rn).replace('.', '').replace('-', '')

    # get an index in that string to multipy the number by
    i = n2 % 10
    mult = int(s_rn[i])
    rn *= mult

    # limit it to 2**16
    rn = rn % (2 ** 16)

    return int(rn)

def rng_between(lower: int, upper: int) -> int:

    # We can just reuse our base rn function
    rn = rng()

    # This isn't correct yet
    rn = rn % upper
    if rn < lower:
        rn += (lower - rn)

    return rn

def get_n1() -> int:
    return int(time.time() * 1_000_000)

def get_n2() -> int:
    return len(os.getcwd()) * get_n1()

print(rng_between(50, 100))
