class FirstMeta(type):
    def __instancecheck__(cls, arg: object) -> bool:
        raise TypeError('You cannot use this type in isinstance() call')


class First(object, metaclass=FirstMeta):
    ...

# User space:

class MyClass(First): # this looks like a user-define TypedDict subclass
    ...


class MySubClassMeta(FirstMeta):
    def __instancecheck__(cls, arg: object) -> bool:
        return True  # just an override example


class MySubClass(MyClass, metaclass=MySubClassMeta):
    ...

print(isinstance(1, MySubClass))  # True
print(isinstance(1, MyClass))  # TypeError