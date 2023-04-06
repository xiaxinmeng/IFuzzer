import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_duplicate_function_equality():

    def duplicate():
        """my docstring"""
        return 3
    FunctionPropertiesTest.assertNotEqual(FunctionPropertiesTest.b, duplicate)

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
FunctionPropertiesTest.setUp()
test_duplicate_function_equality()
