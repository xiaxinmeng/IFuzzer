import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_set_docstring_attr():
    FunctionDocstringTest.assertEqual(FunctionDocstringTest.b.__doc__, None)
    docstr = 'A test method that does nothing'
    FunctionDocstringTest.b.__doc__ = docstr
    FunctionDocstringTest.F.a.__doc__ = docstr
    FunctionDocstringTest.assertEqual(FunctionDocstringTest.b.__doc__, docstr)
    FunctionDocstringTest.assertEqual(FunctionDocstringTest.fi.a.__doc__, docstr)
    FunctionDocstringTest.cannot_set_attr(FunctionDocstringTest.fi.a, '__doc__', docstr, AttributeError)

FunctionDocstringTest = test_funcattrs.FunctionDocstringTest()
FunctionDocstringTest.setUp()
test_set_docstring_attr()
