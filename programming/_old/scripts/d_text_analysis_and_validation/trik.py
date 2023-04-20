# Trik
# https://dmoj.ca/problem/coci06c5p1/resubmit/3446146

moves = input()
cup = 1

for move in moves:
    
    if move == 'A':
        if cup == 1:
            cup = 2
        elif cup == 2:
            cup = 1
            
    elif move == 'B':
        if cup == 2:
            cup = 3
        elif cup == 3:
            cup = 2
    
    else:
        if cup == 1:
            cup = 3
        elif cup == 3:
            cup = 1

print(cup)