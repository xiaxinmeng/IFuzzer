import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test___globals__():
    FunctionPropertiesTest.assertIs(FunctionPropertiesTest.b.__globals__, globals())
    FunctionPropertiesTest.cannot_set_attr(FunctionPropertiesTest.b, '__globals__', 2, (AttributeError, TypeError))

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
FunctionPropertiesTest.setUp()
test___globals__()
