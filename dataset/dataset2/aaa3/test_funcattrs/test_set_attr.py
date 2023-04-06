import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test_set_attr():
    ArbitraryFunctionAttrTest.b.known_attr = 7
    ArbitraryFunctionAttrTest.assertEqual(ArbitraryFunctionAttrTest.b.known_attr, 7)
    try:
        ArbitraryFunctionAttrTest.fi.a.known_attr = 7
    except AttributeError:
        pass
    else:
        ArbitraryFunctionAttrTest.fail('setting attributes on methods should raise error')

ArbitraryFunctionAttrTest = test_funcattrs.ArbitraryFunctionAttrTest()
ArbitraryFunctionAttrTest.setUp()
test_set_attr()
