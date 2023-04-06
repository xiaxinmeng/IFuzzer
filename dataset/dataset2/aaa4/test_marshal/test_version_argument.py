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

def test_version_argument():
    BugsTestCase.assertEqual(marshal.loads(marshal.dumps(5, 0)), 5)
    BugsTestCase.assertEqual(marshal.loads(marshal.dumps(5, 1)), 5)

BugsTestCase = test_marshal.BugsTestCase()
test_version_argument()
