import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test___func___non_method():
    InstancemethodAttrTest.fi.id = types.MethodType(id, InstancemethodAttrTest.fi)
    InstancemethodAttrTest.assertEqual(InstancemethodAttrTest.fi.id(), id(InstancemethodAttrTest.fi))
    try:
        InstancemethodAttrTest.fi.id.unknown_attr
    except AttributeError:
        pass
    else:
        InstancemethodAttrTest.fail('using unknown attributes should raise AttributeError')
    InstancemethodAttrTest.cannot_set_attr(InstancemethodAttrTest.fi.id, 'unknown_attr', 2, AttributeError)

InstancemethodAttrTest = test_funcattrs.InstancemethodAttrTest()
InstancemethodAttrTest.setUp()
test___func___non_method()
