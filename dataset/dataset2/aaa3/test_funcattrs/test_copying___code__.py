import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_copying___code__():

    def test():
        pass
    FunctionPropertiesTest.assertEqual(test(), None)
    test.__code__ = FunctionPropertiesTest.b.__code__
    FunctionPropertiesTest.assertEqual(test(), 3)

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
FunctionPropertiesTest.setUp()
test_copying___code__()
