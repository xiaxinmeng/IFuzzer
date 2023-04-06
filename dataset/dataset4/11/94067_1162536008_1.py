class Test2:
    id: int = 1
    @property
    def id(self): pass
print(Test2.__dict__)