from weakref import proxy

class Alpha:
    def __len__(self):
        return 3
    def __reversed__(self):
        return iter('cba')
    def __hash__(self):
        return hash('abc')

a = Alpha()

# Direct use of the instance works
print(len(a))
print(list(reversed(a)))
print(hash(a))

# Proxies can use the dunder methods directly
r = proxy(a)
print(r.__len__())
print(list(r.__reversed__()))
print(r.__hash__())