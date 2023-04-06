import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_delete_docstring():
    FunctionDocstringTest.b.__doc__ = 'The docstring'
    del FunctionDocstringTest.b.__doc__
    FunctionDocstringTest.assertEqual(FunctionDocstringTest.b.__doc__, None)

FunctionDocstringTest = test_funcattrs.FunctionDocstringTest()
FunctionDocstringTest.setUp()
test_delete_docstring()
