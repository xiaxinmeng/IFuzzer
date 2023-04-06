import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_dir_includes_correct_attrs():
    FunctionPropertiesTest.b.known_attr = 7
    FunctionPropertiesTest.assertIn('known_attr', dir(FunctionPropertiesTest.b), 'set attributes not in dir listing of method')
    FunctionPropertiesTest.F.a.known_attr = 7
    FunctionPropertiesTest.assertIn('known_attr', dir(FunctionPropertiesTest.fi.a), 'set attribute on function implementations, should show up in next dir')

FunctionPropertiesTest = test_funcattrs.FunctionPropertiesTest()
FunctionPropertiesTest.setUp()
test_dir_includes_correct_attrs()
