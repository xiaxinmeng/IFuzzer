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

def test_write_long_to_file():
    for v in range(marshal.version + 1):
        _testcapi.pymarshal_write_long_to_file(305419896, os_helper.TESTFN, v)
        with open(os_helper.TESTFN, 'rb') as f:
            data = f.read()
        os_helper.unlink(os_helper.TESTFN)
        CAPI_TestCase.assertEqual(data, b'xV4\x12')

CAPI_TestCase = test_marshal.CAPI_TestCase()
test_write_long_to_file()
