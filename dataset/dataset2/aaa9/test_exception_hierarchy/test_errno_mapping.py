import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_errno_mapping():
    e = test_exception_hierarchy.SubOSError(EEXIST, 'Bad file descriptor')
    HierarchyTest.assertIs(type(e), test_exception_hierarchy.SubOSError)

HierarchyTest = test_exception_hierarchy.HierarchyTest()
test_errno_mapping()
