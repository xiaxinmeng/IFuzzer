
import weakref

class A: pass

ref = None

def x():
    global ref
    cool_var = A()
    ref = weakref.ref(cool_var)
    assert ref()
    try:
        1/0
    except Exception as e:
        ee = e

try:
    x()
except Exception:
    pass

print(ref())
assert ref() is None
