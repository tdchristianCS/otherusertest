#read the number of contestants
n_contestants = int(input())

#make an empty dict for registered
#make an empty dict for finished

registered = {}
finished = {}

#read all the registered and enter them in the dict
#	first time, set to 1
#	after, add 1

for i in range(n_contestants):
    name = input()
    if name not in registered:
        registered[name] = 1
    else:
        registered[name] += 1

#read all the finished and enter them in the dict
#	first time, set to 1
#	after, add 1

for i in range(n_contestants - 1):
    name = input()
    if name not in finished:
        finished[name] = 1
    else:
        finished[name] += 1

# go through all the registered names

for name in registered:

# if that name in finished doesn't have the same value as in registered
# if that name in finished is not equal to that name in registered
    if (name not in finished) or (finished[name] != registered[name]):
    
# that's the person; print them
        print(name)
