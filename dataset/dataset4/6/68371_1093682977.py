from collections import UserDict
class MyDict(UserDict, bar='baz'):
    pass
dictionary = MyDict()  # Expect this to create a new instance of MyDict.