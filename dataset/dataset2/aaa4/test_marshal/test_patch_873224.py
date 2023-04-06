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

def test_patch_873224():
    BugsTestCase.assertRaises(Exception, marshal.loads, b'0')
    BugsTestCase.assertRaises(Exception, marshal.loads, b'f')
    BugsTestCase.assertRaises(Exception, marshal.loads, marshal.dumps(2 ** 65)[:-1])

BugsTestCase = test_marshal.BugsTestCase()
test_patch_873224()
