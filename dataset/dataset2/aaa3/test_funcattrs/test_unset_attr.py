import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_unset_attr():
    for func in [ArbitraryFunctionAttrTest.b, ArbitraryFunctionAttrTest.fi.a]:
        try:
            func.non_existent_attr
        except AttributeError:
            pass
        else:
            ArbitraryFunctionAttrTest.fail('using unknown attributes should raise AttributeError')

ArbitraryFunctionAttrTest = test_funcattrs.ArbitraryFunctionAttrTest()
ArbitraryFunctionAttrTest.setUp()
test_unset_attr()
