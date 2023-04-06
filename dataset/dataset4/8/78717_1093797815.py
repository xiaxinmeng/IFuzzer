
import enum

class MyEnum(enum.Enum):
    FOO = "foo"

    @classmethod
    def _missing_(cls, value):
        return 5

print(MyEnum('bar'))  # output: 5
