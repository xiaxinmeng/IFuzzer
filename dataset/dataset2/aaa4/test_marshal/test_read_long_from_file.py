from test import support
from test.support import os_helper
import array
import io
import marshal
import sys
import unittest
import os
import types
import _testcapi
import test_marshal

def test_read_long_from_file():
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(b'xV4\x12xxxx')
    (r, p) = _testcapi.pymarshal_read_long_from_file(os_helper.TESTFN)
    os_helper.unlink(os_helper.TESTFN)
    CAPI_TestCase.assertEqual(r, 305419896)
    CAPI_TestCase.assertEqual(p, 4)
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(b'V4\x12')
    with CAPI_TestCase.assertRaises(EOFError):
        _testcapi.pymarshal_read_long_from_file(os_helper.TESTFN)
    os_helper.unlink(os_helper.TESTFN)

CAPI_TestCase = test_marshal.CAPI_TestCase()
test_read_long_from_file()
