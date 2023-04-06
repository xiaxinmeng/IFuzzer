class C:
    def __init__(self, *a): self.a = a
    def __hash__(self): return hash(self.a[0])
    def __eq__(self, o): return self.a[0] == o.a[0]
    def __repr__(self): return f"C{self.a}"