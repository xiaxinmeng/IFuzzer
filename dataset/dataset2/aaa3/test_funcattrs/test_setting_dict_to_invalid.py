import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_setting_dict_to_invalid():
    FunctionDictsTest.cannot_set_attr(FunctionDictsTest.b, '__dict__', None, TypeError)
    from collections import UserDict
    d = UserDict({'known_attr': 7})
    FunctionDictsTest.cannot_set_attr(FunctionDictsTest.fi.a.__func__, '__dict__', d, TypeError)

FunctionDictsTest = test_funcattrs.FunctionDictsTest()
FunctionDictsTest.setUp()
test_setting_dict_to_invalid()
