# this loop is quite complicated
# that's why we create a function to delegate the digit-checking

def find_next_year(year: int) -> int:

    valid = False
    while not valid:
        valid = True
        
        year += 1
        year = str(year)
        for d in year:
            if year.count(d) > 1:
                valid = False
        year = int(year)
        
    return year

print(find_next_year(int(input())))
