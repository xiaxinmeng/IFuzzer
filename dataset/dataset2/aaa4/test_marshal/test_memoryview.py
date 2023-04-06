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

def test_memoryview():
    b = memoryview(b'abc')
    BufferTestCase.helper(b)
    new = marshal.loads(marshal.dumps(b))
    BufferTestCase.assertEqual(type(new), bytes)

BufferTestCase = test_marshal.BufferTestCase()
test_memoryview()
