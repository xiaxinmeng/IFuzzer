import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_func_as_dict_key():
    value = 'Some string'
    d = {}
    d[FunctionDictsTest.b] = value
    FunctionDictsTest.assertEqual(d[FunctionDictsTest.b], value)

FunctionDictsTest = test_funcattrs.FunctionDictsTest()
FunctionDictsTest.setUp()
test_func_as_dict_key()
