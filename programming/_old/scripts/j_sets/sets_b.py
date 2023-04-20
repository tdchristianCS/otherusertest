# Some set operations

# Create a set
s = set()

# Add to a set
s.add(5)

# Note: repeated adding does nothing
s.add(5)
print(len(s)) # 1

# Remove from a set
s.remove(5)
print(len(s)) # 0

# Let's see how to combine sets

set_a = {1, 2, 3, 4, 9, 10, 11}
set_b = {5, 6, 7, 8, 9, 10, 11}

# Combining sets can happen in one of three ways

# UNION: keep all members of both sets
set_a.union(set_b) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# INTERSECTION: keep only the members shared by both sets
set_a.intersection(set_b) # {9, 10, 11}

# DIFFERENCE: keep only the members *unique* to a set
set_a.difference(set_b) # {1, 2, 3, 4}
set_b.difference(set_a) # {5, 6, 7, 8}
