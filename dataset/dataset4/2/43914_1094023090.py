class A:
    js = []
    
    def add (self, j):
        self.js.append(j)

    def clone (self):
        c = A()
        for j in self.js:
            c.add(j)
        return c

a = A()
b = a.clone()
b.add(3)