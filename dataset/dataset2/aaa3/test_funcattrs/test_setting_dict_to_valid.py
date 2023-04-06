import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_setting_dict_to_valid():
    d = {'known_attr': 7}
    FunctionDictsTest.b.__dict__ = d
    FunctionDictsTest.assertIs(d, FunctionDictsTest.b.__dict__)
    FunctionDictsTest.F.a.__dict__ = d
    FunctionDictsTest.assertIs(d, FunctionDictsTest.fi.a.__func__.__dict__)
    FunctionDictsTest.assertIs(d, FunctionDictsTest.fi.a.__dict__)
    FunctionDictsTest.assertEqual(FunctionDictsTest.b.known_attr, 7)
    FunctionDictsTest.assertEqual(FunctionDictsTest.b.__dict__['known_attr'], 7)
    FunctionDictsTest.assertEqual(FunctionDictsTest.fi.a.__func__.known_attr, 7)
    FunctionDictsTest.assertEqual(FunctionDictsTest.fi.a.known_attr, 7)

FunctionDictsTest = test_funcattrs.FunctionDictsTest()
FunctionDictsTest.setUp()
test_setting_dict_to_valid()
