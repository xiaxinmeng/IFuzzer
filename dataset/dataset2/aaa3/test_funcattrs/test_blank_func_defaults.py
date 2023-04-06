import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_blank_func_defaults():
    FunctionPropertiesTest.assertEqual(FunctionPropertiesTest.b.__defaults__, None)
    del FunctionPropertiesTest.b.__defaults__
    FunctionPropertiesTest.assertEqual(FunctionPropertiesTest.b.__defaults__, None)

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
FunctionPropertiesTest.setUp()
test_blank_func_defaults()
