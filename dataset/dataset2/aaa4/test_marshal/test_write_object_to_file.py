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

def test_write_object_to_file():
    obj = ('€', b'abc', 123, 45.6, 7 + 8j, 'long line ' * 1000)
    for v in range(marshal.version + 1):
        _testcapi.pymarshal_write_object_to_file(obj, os_helper.TESTFN, v)
        with open(os_helper.TESTFN, 'rb') as f:
            data = f.read()
        os_helper.unlink(os_helper.TESTFN)
        CAPI_TestCase.assertEqual(marshal.loads(data), obj)

CAPI_TestCase = test_marshal.CAPI_TestCase()
test_write_object_to_file()
