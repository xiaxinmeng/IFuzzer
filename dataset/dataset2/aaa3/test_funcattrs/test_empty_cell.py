import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_empty_cell():

    def f():
        print(a)
    try:
        f.__closure__[0].cell_contents
    except ValueError:
        pass
    else:
        FunctionPropertiesTest.fail("shouldn't be able to read an empty cell")
    a = 12

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
test_empty_cell()
