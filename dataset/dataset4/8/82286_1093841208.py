class C(object):
    def __eq__(self, other):
        print('eq')
        return super().__eq__(other)
    def __hash__(self):
        return -2

d = {-2, C()}