# Epidemiology
# https://dmoj.ca/problem/ccc20j2

# Contributed by Dr. Daniel Zingaro
# Fast version that uses an extra variable to store the previous day's sick
# This saves time on exponentiation for those edge cases
# (To see why, think about exponentiation as an inner loop of multiplication)


P = int(input())
N = int(input())
R = int(input())

day = 0
prev_day_sick = N

while N <= P:
    N = N + prev_day_sick * R
    prev_day_sick = prev_day_sick * R
    day = day + 1

print(day)
