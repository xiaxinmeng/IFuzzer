import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_posix_error():
    e = OSError(EEXIST, 'File already exists', 'foo.txt')
    AttributesTest.assertEqual(e.errno, EEXIST)
    AttributesTest.assertEqual(e.args[0], EEXIST)
    AttributesTest.assertEqual(e.strerror, 'File already exists')
    AttributesTest.assertEqual(e.filename, 'foo.txt')
    if os.name == 'nt':
        AttributesTest.assertEqual(e.winerror, None)

AttributesTest = test_exception_hierarchy.AttributesTest()
test_posix_error()
