def monkeypatch(cls):
    orig = globals()[cls.__name__] # Undocumented magic
    print("Monkeypatch",id(cls),"into",id(orig))
    for attr in dir(cls):
        if not attr.startswith("_"):
            setattr(orig,attr,getattr(cls,attr))
    return orig

class Foo:
    def method1(self):
        print("I am method 1")

print("Foo is currently",id(Foo))
some_object = Foo()

@monkeypatch
class Foo:
    def method2(self):
        print("I am method 2")

print("Foo is now",id(Foo))

some_object.method1()
some_object.method2()