def get_b(self, name):
    print("In get_b")
    if name == "b":
        return "b"
    else:
        raise AttributeError()

class A:
    def __getattribute__(self, name):
        print("In A.__getattribute__")
        if name == "a":
            return "a"
        else:
            type(self).__getattr__ = get_b
            raise AttributeError()

try:
    print(A().b)
except Exception as e:
    print("Raises", type(e), e)
print()
try:
    print(A().b)
except Exception as e:
    print("Raises", type(e), e)