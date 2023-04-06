class A:
    def __getattr__(self, attr_name):
        print(f"looking up {attr_name}")
a = A()
class B:
    a.__foo

# prints: looking up _B__foo