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

def test_large_marshal():
    size = int(1000000.0)
    testString = 'abc' * size
    marshal.dumps(testString)

BugsTestCase = test_marshal.BugsTestCase()
test_large_marshal()
