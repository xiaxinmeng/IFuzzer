class T(tuple):
    def __iter__(self):
        print("__iter__")
        yield self

inst = T(("a", "b"))
print(len(inst))
print(inst[0])
print(inst[1])