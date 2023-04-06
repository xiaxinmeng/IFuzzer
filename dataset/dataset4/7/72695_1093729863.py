import sys
b = {}
for i in range(16):
    b[i] = i
    a = b.copy()
    a.update(b)  # No need to resize
    print(i, sys.getsizeof(a), sys.getsizeof(b))