class X(list):

    def __contains__(self, key):
        print('X contains:', key)


class Y():

    def __init__(self, x):
        self.x = x

    def __getattr__(self, key):
        return getattr(self.x, key)

    def __iter__(self):
        print('Y iter')
        return iter([1,2])

x = X()
y = Y(x)

print('res:', 1 in y)