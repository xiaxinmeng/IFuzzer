
class Foo:
    foo: int
    
    def __init__(self):
        self.foo = 5
    
class Bar(Foo):
    bar: int
    
    def __init__(self, *args, **kwargs):
        if 'bar' in kwargs:
            self.bar = kwargs.pop('bar')
        else:
            *args, self.bar = args
        
        super().__init__(*args, **kwargs)

print([Bar(1), Bar(bar=1)])
