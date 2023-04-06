class myObj(object):
    def __eq__(self, other):
        for i in range(10000): pass # simulate an expensive check
        return False

l=[myObj() for x in range(10000)]