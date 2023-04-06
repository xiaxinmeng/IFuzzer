class Foo:
    def f1(self):
        __obj = object()
        def f2():
            nonlocal __obj
            __obj = []
        f2()
        return isinstance(__obj, list)
        
f = Foo()
print(f.f1())