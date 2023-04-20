# This script demonstrates one way in which a hashmap (a.k.a. a dictionary)
# is superior to an array (a.k.a. a list). A list stores its items in the order
# they were added. So if I ask, "Is Olufemi in the list?" I have to look
# at every item till I find Olufemi. But a dictionary stores items like
# a phonebook, with internal "headings" (which Python worries about, not us).
# So if I ask, "Is Olufemi in the phonebook?" it looks under "O" .. "L" ..
# and finds it instantly. As a result, the hashmap search should be faster.
# (The tradeoff? I takes more memory to store a dictionary than a list.)

import time
import random

# Create empty list and dict
L = []
D = {}

# Fill them with the integers from 0 to 1,000,000
for i in range(1_000_000):
    L.append(i)
    D[i] = 0

# For both these tests, we'll use the extremely rough timing method
# of just taking a "now" snapshot before and after, then subtracting
# the start time from the end time

# We'll do 1,000 trials of looking for a random integer between 1 and 1,000,000
# that's in the data structure and see how long this takes.

start_D = time.time()
for _ in range(1_000):
    n = random.randint(0, 1_000_000)
    n in D # Just writing this causes Python to carry out the check
end_D = time.time()

time_D = end_D - start_D
print(f'Searching D took {time_D:.5f} seconds')

start_L = time.time()
for _ in range(1_000):
    n = random.randint(0, 1_000_000)
    n in L # Just writing this causes Python to carry out the check
end_L = time.time()

time_L = end_L - start_L
print(f'Searching L took {time_L:.5f} seconds')

ratio_D_L = int(time_L / time_D)
print(f'Searching L took ~{ratio_D_L:,}x as long')
