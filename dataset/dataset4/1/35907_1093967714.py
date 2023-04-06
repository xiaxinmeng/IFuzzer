class A:
    def __init__(self):
        self.a = 0

a = A()
for i in xrange(2**20):
    a.a = i