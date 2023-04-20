# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    # cat!
    # 3 1 20
    
    result = ''
    for letter in text:
        if letter.isalpha():
            letter = letter.lower() # lowercase for consistency
            ascii = ord(letter) # a = 97, b = 98, etc.
            ascii -= 96         # a = 1, b = 2, etc.
            result += str(ascii) + ' ' # add a space as in example
    
    return result[:-1] # subtract the last extra space...
