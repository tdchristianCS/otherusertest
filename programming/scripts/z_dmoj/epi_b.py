# Epidemiology
# https://dmoj.ca/problem/ccc20j2

# fast (if inelegant) solution using geometric series math

import math
P = int(input())
N = int(input())
R = int(input())

if R == 1:
    days = (P + 1 - N) / N
    print(math.ceil(days))

elif N >= P:
    print(1)
    
else:
    days = math.log10(P / N) / math.log10(R)
    
    floor = math.floor(days)
    ceil = math.ceil(days)
    
    tn_low = N * ((1 - R ** (floor + 1)) / (1 - R))
    
    if tn_low > P:
        print(floor)
    else:
        print(ceil)
