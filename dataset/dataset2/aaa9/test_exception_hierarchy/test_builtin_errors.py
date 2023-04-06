import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_builtin_errors():
    HierarchyTest.assertEqual(OSError.__name__, 'OSError')
    HierarchyTest.assertIs(IOError, OSError)
    HierarchyTest.assertIs(EnvironmentError, OSError)

HierarchyTest = test_exception_hierarchy.HierarchyTest()
test_builtin_errors()
