from types import new_class
MyDerived = new_class("MyDerived", (), dict(metaclass=metaclass_callable))

print(type(MyDerived))