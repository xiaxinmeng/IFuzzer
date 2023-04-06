import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_unassigned_dict():
    FunctionDictsTest.assertEqual(FunctionDictsTest.b.__dict__, {})

FunctionDictsTest = test_funcattrs.FunctionDictsTest()
FunctionDictsTest.setUp()
test_unassigned_dict()
