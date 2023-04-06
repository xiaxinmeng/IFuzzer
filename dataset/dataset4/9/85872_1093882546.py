
class C:
    def __add__(self, other):
        return "from class"


c = C()
print(c + c)  # prints "from class"

c.__add__ = lambda other: "from instance"
print(c.__add__(c))  # prints "from instance"
print(type(c).__add__(c, c))  # prints "from class"

print(c + c)  # prints "from class"!
