import unittest
from test.support import import_helper
import types
import test_xxlimited

def test_roj():
    with TestXXLimited35.assertRaises(SystemError):
        TestXXLimited35.module.roj(0)

TestXXLimited35 = test_xxlimited.TestXXLimited35()
test_roj()
