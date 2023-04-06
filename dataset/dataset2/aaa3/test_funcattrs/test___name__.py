import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test___name__():
    FunctionPropertiesTest.assertEqual(FunctionPropertiesTest.b.__name__, 'b')
    FunctionPropertiesTest.b.__name__ = 'c'
    FunctionPropertiesTest.assertEqual(FunctionPropertiesTest.b.__name__, 'c')
    FunctionPropertiesTest.b.__name__ = 'd'
    FunctionPropertiesTest.assertEqual(FunctionPropertiesTest.b.__name__, 'd')
    FunctionPropertiesTest.cannot_set_attr(FunctionPropertiesTest.b, '__name__', 7, TypeError)
    s = 'def f(): pass\nf.__name__'
    exec(s, {'__builtins__': {}})
    FunctionPropertiesTest.assertEqual(FunctionPropertiesTest.fi.a.__name__, 'a')
    FunctionPropertiesTest.cannot_set_attr(FunctionPropertiesTest.fi.a, '__name__', 'a', AttributeError)

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
FunctionPropertiesTest.setUp()
test___name__()
