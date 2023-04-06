@public
class Foo:
    pass

public(qux=3)

print(qux)

@public
def zzz():
    pass

public(jix=1, jox=2, jrx=3)

print(__all__)
print(jix, jox, jrx)