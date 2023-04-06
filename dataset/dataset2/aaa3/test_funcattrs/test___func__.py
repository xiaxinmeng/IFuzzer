import types
import unittest
from collections import UserDict
import time
import test_funcattrs

def test___func__():
    InstancemethodAttrTest.assertEqual(InstancemethodAttrTest.fi.a.__func__, InstancemethodAttrTest.F.a)
    InstancemethodAttrTest.cannot_set_attr(InstancemethodAttrTest.fi.a, '__func__', InstancemethodAttrTest.F.a, AttributeError)

InstancemethodAttrTest = test_funcattrs.InstancemethodAttrTest()
InstancemethodAttrTest.setUp()
test___func__()
