# Epidemiology
# https://dmoj.ca/problem/ccc20j2

# slow solution that works in PyPy but times out in Python 3
P = int(input())
N = int(input())
R = int(input())
days = 0
sick = N

while sick <= P:
    days += 1
    sick += N * (R ** days)

print(days)

