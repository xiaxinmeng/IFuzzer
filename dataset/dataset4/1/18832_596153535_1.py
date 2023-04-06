class C(ChainMap):
    def __ror__(self, other):
        return super().__ror__(other)

c1 = ChainMap()
c2 = C()

print(c1 | c2)  # C(ChainMap({}))    # !?
print(c2 | c1)  # C({})