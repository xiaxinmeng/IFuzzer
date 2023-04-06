import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test___class__():
    InstancemethodAttrTest.assertEqual(InstancemethodAttrTest.fi.a.__InstancemethodAttrTest__.__class__, InstancemethodAttrTest.F)
    InstancemethodAttrTest.cannot_set_attr(InstancemethodAttrTest.fi.a, '__class__', InstancemethodAttrTest.F, TypeError)

InstancemethodAttrTest = test_funcattrs.InstancemethodAttrTest()
InstancemethodAttrTest.setUp()
test___class__()
