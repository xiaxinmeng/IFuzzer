class DefaultBox(Generic[T]):
    def __init__(self, value: T | None = None):
        self.value = (
            value if value is not None else  # the arg
            self.__orig_class__.__args__[0]()  # or the default for the type argument 
        )

int_box = DefaultBox[int]()
print(int_box.value)  # should print 0
str_box = DefaultBox[str](value="this")
print(str_box.value)  # should print this