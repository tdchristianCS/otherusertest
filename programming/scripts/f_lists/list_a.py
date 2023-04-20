# a list is a sequence of values
L = [1, 5, 4, 6, 7, 8]

# we can index it
L[0] == 1
L[5] == 8

# we can slice it
L[2:4] == [4, 6]

# we can use empty slice to copy it
L[:] = [1, 5, 4, 6, 7, 8]

# we can iterate through it
for item in L:
    print(item)

# 1
# 5
# 4
# 6
# 7
# 8

# dir(list)
# [... 'append', 'clear', 'copy', 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort']

# appending
L = [5, 6, 7]
L.append(8)
L == [5, 6, 7, 8]

# extending
L1 = [5, 6, 7]
L2 = [1, 2, 3]
L1.extend(L2)
L1 == [5, 6, 7, 1, 2, 3]

# sorting
L = [7, 5, 6, 2]
L.sort()
L == [2, 5, 6, 7]

# reversing
L = [1, 4, 3, 5]
L.reverse()
L == [5, 3, 4, 1]

# write a function that sums a list
L = [5, 8, 9, 10]

total = 0
for item in L:
    total = total + item
print(total)
