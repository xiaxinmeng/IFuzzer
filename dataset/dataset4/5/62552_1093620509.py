import collections
import copy

count = collections.Counter()
count.b = 3
print(count.b) # prints 3

count_copy = copy.deepcopy(count)
print(count_copy.b) # raise AttributeError: 'Counter' object has no attribute 'b'