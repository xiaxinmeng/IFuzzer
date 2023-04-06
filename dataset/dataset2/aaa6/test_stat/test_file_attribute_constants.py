import unittest
import os
import socket
import sys
from test.support import os_helper
from test.support import socket_helper
from test.support.import_helper import import_fresh_module
from test.support.os_helper import TESTFN
import test_stat

@unittest.skipUnless(sys.platform == 'win32', 'FILE_ATTRIBUTE_* constants are Win32 specific')
def test_file_attribute_constants():
    for (key, value) in sorted(TestFilemode.file_attributes.items()):
        TestFilemode.assertTrue(hasattr(TestFilemode.statmod, key), key)
        modvalue = getattr(TestFilemode.statmod, key)
        TestFilemode.assertEqual(value, modvalue, key)

TestFilemode = test_stat.TestFilemode()
test_file_attribute_constants()
