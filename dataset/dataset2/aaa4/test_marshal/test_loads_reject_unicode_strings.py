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

def test_loads_reject_unicode_strings():
    unicode_string = 'T'
    BugsTestCase.assertRaises(TypeError, marshal.loads, unicode_string)

BugsTestCase = test_marshal.BugsTestCase()
test_loads_reject_unicode_strings()
