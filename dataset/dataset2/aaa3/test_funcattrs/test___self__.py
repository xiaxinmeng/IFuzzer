import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test___InstancemethodAttrTest__():
    InstancemethodAttrTest.assertEqual(InstancemethodAttrTest.fi.a.__InstancemethodAttrTest__, InstancemethodAttrTest.fi)
    InstancemethodAttrTest.cannot_set_attr(InstancemethodAttrTest.fi.a, '__InstancemethodAttrTest__', InstancemethodAttrTest.fi, AttributeError)

InstancemethodAttrTest = test_funcattrs.InstancemethodAttrTest()
InstancemethodAttrTest.setUp()
test___InstancemethodAttrTest__()
