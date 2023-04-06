d1 = deque()
d2 = deque()

class A:
    def __eq__(self, other):
        d1.pop()
        d1.appendleft(1)
        return 1

d1.extend((0, 1))
d2.extend((A(), 1))