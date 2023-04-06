import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_func_attribute():

    def f():
        pass
    c = classmethod(f)
    StaticMethodAttrsTest.assertTrue(c.__func__ is f)
    s = staticmethod(f)
    StaticMethodAttrsTest.assertTrue(s.__func__ is f)

StaticMethodAttrsTest = test_funcattrs.StaticMethodAttrsTest()
test_func_attribute()
