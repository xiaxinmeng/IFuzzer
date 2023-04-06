class MC(type):
    def __new__(mcs, name, bases, attrs):
        for name, attr in attrs.items():
            pass
        return super(MC, mcs).__new__(mcs, name, bases, attrs)

class C(metaclass=MC):
    a = None

print(C.__name__)