text = input('Enter some text: ').strip()
back = ''

for c in text:
    if c == '#':
        back = back[:-1]
    else:
        back += c

print(back)
