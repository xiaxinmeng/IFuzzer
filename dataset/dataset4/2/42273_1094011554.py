class H(set):
    def __hash__(self):return id(self)
s=H()

f=set()
f.add(s)
f.remove(s) #  this fails