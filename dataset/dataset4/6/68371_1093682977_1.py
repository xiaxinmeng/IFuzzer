from collections import UserDict
class MyDict(UserDict, bar='baz'):
    pass
dictionary = MyDict()  # This call fails because UserDict inherits from ABCMeta