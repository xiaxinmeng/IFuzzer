import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_delete_unknown_attr():
    try:
        del ArbitraryFunctionAttrTest.b.unknown_attr
    except AttributeError:
        pass
    else:
        ArbitraryFunctionAttrTest.fail('deleting unknown attribute should raise TypeError')

ArbitraryFunctionAttrTest = test_funcattrs.ArbitraryFunctionAttrTest()
test_delete_unknown_attr()
