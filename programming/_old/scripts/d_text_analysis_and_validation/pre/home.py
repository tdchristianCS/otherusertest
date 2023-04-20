HOME = '&'
END = '*'
BACK = '#'

text = input('Enter some text: ').strip()
s = ''
i = 0

for c in text:
    
    if c == HOME:
        i = 0
    elif c == END:
        i = len(s)
    elif c == BACK:
        s = s[:i-1] + s[i:]
        i -= 1
    else:
        s = s[:i] + c + s[i:]
        i += 1

print(s)

        
