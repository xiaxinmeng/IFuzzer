import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_windows_error():
    if os.name == 'nt':
        AttributesTest.assertIn('winerror', dir(OSError))
    else:
        AttributesTest.assertNotIn('winerror', dir(OSError))

AttributesTest = test_exception_hierarchy.AttributesTest()
test_windows_error()
