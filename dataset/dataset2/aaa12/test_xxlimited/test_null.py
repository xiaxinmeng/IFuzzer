import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_null():
    null1 = TestXXLimited35.module.Null()
    null2 = TestXXLimited35.module.Null()
    TestXXLimited35.assertNotEqual(null1, null2)

TestXXLimited35 = test_xxlimited.TestXXLimited35()
test_null()
