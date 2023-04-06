
import enum, pickle

class MyInt(int):
    pass
    # work-around: __reduce_ex__ = int.__reduce_ex__

class MyEnum(MyInt, enum.Enum):
    A = 1

pickle.dumps(MyEnum.A)
