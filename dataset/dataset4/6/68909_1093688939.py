class A:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)

class B(A):
    'Track the number of odds'
    def __init__(self):
        A.__init__(self)
        self.odds = 0
    def add(self, x):
        A.add(self, x)
        self.odds += (x % 2)

b = B()
b.add(1)
b.add(2)
b.add(3)
b.add(4)
A.add(b, 5)
assert b.odds == sum(x%1 for x in b.data), 'OMG, B is broken!'