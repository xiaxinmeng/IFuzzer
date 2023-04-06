import traceback
import sys

from PyQt5.QtCore import Qt

class MetaA(type):
    pass

class A(metaclass=MetaA):
    pass

class MetaB(type):
    pass

class B(metaclass=MetaB):
    pass

for ClassB in B, Qt:

    print("Trying class %s" % (ClassB.__name__, ))

    class MyMeta(type(A), type(ClassB)):
        def __setattr__(cls, key, value):
            print(cls)
            super(type, cls).__setattr__(key, value)

    class MyClass(A, ClassB, metaclass=MyMeta):
        pass