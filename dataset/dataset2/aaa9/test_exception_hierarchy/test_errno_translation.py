import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

@unittest.skipUnless(os.name == 'nt', 'Windows-specific test')
def test_errno_translation():
    e = OSError(0, 'File already exists', 'foo.txt', 183)
    AttributesTest.assertEqual(e.winerror, 183)
    AttributesTest.assertEqual(e.errno, EEXIST)
    AttributesTest.assertEqual(e.args[0], EEXIST)
    AttributesTest.assertEqual(e.strerror, 'File already exists')
    AttributesTest.assertEqual(e.filename, 'foo.txt')

AttributesTest = test_exception_hierarchy.AttributesTest()
test_errno_translation()
