import sys

def size(obj):
    print(sys.getsizeof(obj))

size({})
size({i:i for i in range(3)})
size({i:i for i in range(10)})
size({i:i for i in range(100)})