import os
import pathlib
import enum

class MyEnum(enum.Enum):
    RED = 'red'

    def __fspath__(self):
        return self.name

print(os.fspath(MyEnum.RED))
print(pathlib.Path.home() / MyEnum.RED)