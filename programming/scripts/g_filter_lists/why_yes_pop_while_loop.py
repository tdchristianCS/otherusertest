L = [1, 2, 3, 4, 5, 6, 7]
while len(L) > 0:
    L.pop()
print(L)

# this works because it never involves an index.
# a while loop uses a goal instead of an index,
# so we can say: "we don't care where we are in the list;
# just keep removing something until the list is empty."
# (specifically, pop() removes the last item by default)
