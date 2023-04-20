# Martha takes a jar of quarters to the casino with the intention of becoming rich. She plays three machines in turn. Unknown to her, the machines are entirely predictable. Each play costs one quarter. The first machine pays 30 quarters every 35 t h 35^{th} time it is played; the second machine pays 60 60 quarters every 100 t h 100^{th} time it is played; the third pays 9 9 quarters every 10 t h 10^{th} time it is played.

# Your program should take as input the number of quarters in Martha's jar (there will be at least one and fewer than 1000 1000 ), and the number of times each machine has been played since it last paid.

m_quarters = int(input())
A_plays_since_paid = int(input())
B_plays_since_paid = int(input())
C_plays_since_paid = int(input())

total_plays = 0

on_machine = 'A'

while m_quarters > 0:
    m_quarters -= 1
    total_plays += 1
    
    if on_machine == 'A':
        A_plays_since_paid += 1
        if A_plays_since_paid == 35:
            m_quarters += 30
            A_plays_since_paid = 0
        
        on_machine = 'B'
        
    elif on_machine == 'B':
        B_plays_since_paid += 1
        if B_plays_since_paid == 100:
            m_quarters += 60
            B_plays_since_paid = 0
        on_machine = 'C'
    
    elif on_machine == 'C':
        C_plays_since_paid += 1
        if C_plays_since_paid == 10:
            m_quarters += 9
            C_plays_since_paid = 0
        on_machine = 'A'
    
print(f'Martha plays {total_plays} times before going broke.')
