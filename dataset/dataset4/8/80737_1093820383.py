class ObjectCounter(object):
    count = 0
    def __init__(self):
        type(self).count += 1
    def __del__(self):
        L = [self]
        type(self).count -= 1
L = None
for i in range(60):
    L = [L, ObjectCounter()]
del L
print(ObjectCounter.count)