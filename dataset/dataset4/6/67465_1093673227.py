import traceback
import sys

class MyMeta(type):
    def __setattr__(cls, key, value):
        print("OK")

class MyClass(metaclass=MyMeta):
    pass

MyClass.abc = 12 # outputs "OK"
try:
    print(MyClass.abc)
except:
    traceback.print_exc(file=sys.stdout) # exception comes here as expected

type.__setattr__(MyClass, 'test', 42) # outputs nothing
print(MyClass.test) # outputs "42"