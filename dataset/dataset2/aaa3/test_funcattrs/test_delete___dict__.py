import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_delete___dict__():
    try:
        del FunctionDictsTest.b.__dict__
    except TypeError:
        pass
    else:
        FunctionDictsTest.fail('deleting function dictionary should raise TypeError')

FunctionDictsTest = test_funcattrs.FunctionDictsTest()
FunctionDictsTest.setUp()
test_delete___dict__()
