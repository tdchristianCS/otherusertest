# let's try to remove every item from this list

L = [1, 2, 3, 4, 5, 6, 7]
for item in L:
    L.remove(item)
print(L)

# Does this empty the list?
# No!... It leaves [2, 4, 6]!!
# Why?

# The reason is that 'for item in L' actually keeps an invisible index
# Even though you remove items, indices always start at 0
# Take a look below

# before we start, here's the list
# items   1 2 3 4 5 6 7
# indices 0 1 2 3 4 5 6

# first iteration of the loop
    # i = 0
    # L         1 2 3 4 5 6 7
    # indices   0 1 2 3 4 5 6

# i == 0 so it removes the item at index 0
# but that doesn't mean there is no longer an index 0... things just shift

# second iteration of the loop
    # i = 1
    # L         2 3 4 5 6 7
    # indices   0 1 2 3 4 5

# i == 1 so it removes the item at index 1
# ... leaving the 2 at index 0

# third iteration of the loop
    # i = 2
    # L         2 4 5 6 7
    # indices   0 1 2 3 4

# i == 2 so it removes the item at index 2
# ... leaving the 2 and the 4 at indices 0 and 1

# fourth iteration of the loop
    # i = 3
    # L         2 4 6 7
    # indices   0 1 2 3

# i == 3 so it removes the item at index 3

    # L         2 4 6
    # indices   0 1 2

# i is now greater than the length of the list, so Python stops the loop
# and it contentedly gives us back our list as [2, 4, 6]

# Takeaway: do not remove items from a list using a for loop
# modifying indices while looping: "not even once"

