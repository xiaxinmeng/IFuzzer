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

def test_invalid_longs():
    invalid_string = b'l\x02\x00\x00\x00\x00\x00\x00\x00'
    BugsTestCase.assertRaises(ValueError, marshal.loads, invalid_string)

BugsTestCase = test_marshal.BugsTestCase()
test_invalid_longs()
