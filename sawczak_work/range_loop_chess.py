# 2-dimensional data is achieved using nested lists
# the level of nesting = the number of axes
# a chess board has 2 dimensions so we have list within list

CHESSBOARD = [
    ['R', 'T', 'B', 'K', 'Q', 'B', 'T', 'R',],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',], 
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',], 
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',],
    ['R', 'T', 'B', 'Q', 'K', 'B', 'T', 'R',],
]

# only 8 items in CHESSBOARD
print(len(CHESSBOARD))

# but each of those itself has 8 items
print(len(CHESSBOARD[0]))

# print each row on its own line
for row in CHESSBOARD:
    print(row)

# iterate through every column and row
for row in CHESSBOARD:
    for col in row:
        print(col)

# we can also use a range loop to identify each piece by column and row
for row in range(8):
    for col in range(8):
        piece = CHESSBOARD[row][col]
        print(f'Piece at row {row}, col {col} = {piece}')

# Can we access specific rows and cols?
# Sure, let's let the user move a piece

for row in CHESSBOARD:
    print(row)

row = int(input('Enter the row of the piece you want to move: '))
col = int(input('Enter the col of the piece you want to move: '))

piece = CHESSBOARD[row][col]

row2 = int(input('Enter the row where you want to move it to: '))
col2 = int(input('Enter the col where you want to move it to: '))

CHESSBOARD[row][col] = ' '
CHESSBOARD[row2][col2] = piece

for row in CHESSBOARD:
    print(row)
