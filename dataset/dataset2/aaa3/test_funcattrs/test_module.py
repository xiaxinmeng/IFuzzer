import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_module():
    FunctionPropertiesTest.assertEqual(FunctionPropertiesTest.b.__module__, __name__)

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
FunctionPropertiesTest.setUp()
test_module()
