import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_try_except():
    filename = 'some_hopefully_non_existing_file'
    try:
        open(filename)
    except FileNotFoundError:
        pass
    else:
        HierarchyTest.fail('should have raised a FileNotFoundError')
    HierarchyTest.assertFalse(os.path.exists(filename))
    try:
        os.unlink(filename)
    except FileNotFoundError:
        pass
    else:
        HierarchyTest.fail('should have raised a FileNotFoundError')

HierarchyTest = test_exception_hierarchy.HierarchyTest()
test_try_except()
