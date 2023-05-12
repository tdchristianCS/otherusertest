import math
import time
import os
import random

# This code tries to import progress bar
# and sets a flag True/False for whether it was successful
# To use this feature, do pip install progress
try:
    from progress.bar import ChargingBar
    PROGRESS_BAR = True
except:
    PROGRESS_BAR = False

RNG_LIMIT = 2 ** 16
LEN_CWD = len(os.getcwd())

def rng() -> int:
    """
    Return a random number up to 2 ** 16.
    """
    rn = 1
    n1 = get_n1()
    n2 = get_n2()

    rn *= (1 + (n1 * math.pi))

    # turn that into a string, and take the part after the period
    s_rn = str(rn).replace('.', '').replace('-', '')

    # get an index in that string to multipy the number by
    i = n2 % 10
    mult = int(s_rn[i])
    rn *= (1 + mult)

    # limit it to 2**16
    rn = rn % RNG_LIMIT

    return round(rn)

def rng_between(lower: int, upper: int) -> int:
    """
    Return a random between lower and upper, inclusive.
    Note that the lower and upper bounds are half as likely to appear
    for stupid reasons. TODO
    """

    # We can just reuse our base rn function
    rn = rng()

    upper += 1

    # This seems to work but very often gives even numbers
    # rn = rn % upper
    # if rn < lower:
    #     rn += lower

    # Scale it to between 0...1 by dividing it by its maximum value
    zero_to_one = rn / RNG_LIMIT

    # Scale it to lower...upper bounds via this math
    scaled = zero_to_one * (upper - lower)
    scaled = scaled + lower

    return int(scaled)

def rng_choose(L: list) -> object:
    """
    Return a random item from the given list.
    The first and last items are less likely to appear. TODO
    """

    # How can you pick a random object from a list?
    # Use our existing functions

    rn_index = rng_between(0, len(L) - 1)
    rn_item = L[rn_index]
    return rn_item

def get_n1() -> int:
    """
    Return a random integer based on the current time.
    """
    return int(time.time() * 1_000_000)

def get_n2() -> int:
    """
    Return a random integer based on the current working directory
    and time.
    """
    return LEN_CWD * get_n1()

def test_randomness(rng_function: callable) -> None:
    """
    Execute and print a report of the random distribution
    of the rng_between function.
    """

    print(f'Testing randomness of {rng_function.__name__}')

    # empty dictionary that will track how often
    # each number appears
    frequencies = {}

    n_trials = 1_000_000

    # Update every 10% of the way
    update_every = n_trials // 10

    if PROGRESS_BAR:
        # If using a progress bar, update every 1% of the way
        update_every = update_every // 10
        bar = ChargingBar('Progress', max=(n_trials // update_every))

    for i in range(n_trials):
        rn = rng_function(1, 10)

        # if we haven't seen it yet, we need to start the key at 0
        if rn not in frequencies:
            frequencies[rn] = 0
        
        # tally that we've seen it
        frequencies[rn] += 1

        # little progress report for the longer trials...
        if (i + 1) % update_every == 0:
            if PROGRESS_BAR:
                bar.next()
            else:
                fraction = (i + 1) / n_trials * 100
                print(f'Generated {fraction}% of the random numbers')
    
    # Sort the numbers and print the % of each one
    print()
    for number in sorted(frequencies):
        percentage = frequencies[number] / n_trials * 100

        # the :.2f means 'print this up to 2 decimals'
        print(f'{number} : {percentage:.1f} %')
    print()


# print(rng())
# print(rng_between(1, 100))

# items = ['Brandon', 'Daniel', 'Jaewook', 'Vol', 'Jack']
# print(rng_choose(items))

test_randomness(random.randint)
test_randomness(rng_between)
