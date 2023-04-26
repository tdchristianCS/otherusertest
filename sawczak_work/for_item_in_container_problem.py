
# Can we filter by removing instead of by adding to a new list?
# We can remove something in two ways:
# pop(index)
# remove(item)
# let's try remove

ages = [16, 14, 15, 16, 17, 9, 15, 21, 2, 3, 4, 5, 20, 24, 18, 33, 5, 11, 13, 29, 26]

for age in ages:
    if age < 18:
        ages.remove(age)

print(ages)

# What's the problem?
# The loop actually works by looking at indices, e.g. ages[0], ages[1]
# If we remove a value, all the values shift over to the left and some can then get missed
