import time
    
def test_list():
    print('starting to append to list')
    start = time.time()
    L = []
    for i in range(10000000): # 10 million
        L.append(i + 1)
    end = time.time()
    print(f'appending 10000000 items to list took {(end - start):.2} seconds')

    print()

    print('starting to check list')
    start = time.time()
    for i in range(50):
        if 0 in L:
            break
    end = time.time()

    print(f'Checking list 50 times took {(end - start):.2} seconds')

def test_set():
    print('starting to add to set')
    start = time.time()
    s = set()
    for i in range(10000000):
        s.add(i + 1)
    end = time.time()
    print(f'adding 10000000 items to set took {(end - start):.2} seconds')

    print()

    print('starting to check in set')
    start = time.time()
    for i in range(50000):
        if 0 in s:
            break
    end = time.time()
    print(f'checking set 50000 times took {(end - start):.2} seconds')

def run():
    print('Comparing list and set times')
    print('We will add 10 million items to a list and to a set')
    print('Then we will check a fixed number of times whether 0 is in either one')
    print()
    input('Hit enter to start')
    print()
    test_list()
    print()
    test_set()


run()
