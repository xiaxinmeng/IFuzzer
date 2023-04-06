import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_error():
    with TestXXLimited.assertRaises(TestXXLimited.module.Error):
        raise TestXXLimited.module.Error

TestXXLimited = test_xxlimited.TestXXLimited()
test_error()
