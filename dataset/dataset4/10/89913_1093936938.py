import copy, array
a = array.array('i', [1, 2])
b = copy.copy(a)
a[0] = 3
print(a)
print(b)