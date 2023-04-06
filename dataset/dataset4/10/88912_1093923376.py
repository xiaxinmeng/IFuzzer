class Foo(dict):
    def __getitem__(self, index):
        return 5 if index == 'y' else super().__getitem__(index)
 
exec('print(y)', Foo())
exec('global y; print(y)', Foo())
exec('''
class UsesLOAD_NAME:
    global y
    print(y)''', Foo())
exec('''
class UsesLOAD_NAME:
    print(y)''', Foo())