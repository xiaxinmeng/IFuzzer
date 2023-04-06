import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_select_error():
    HierarchyTest.assertIs(select.error, OSError)

HierarchyTest = test_exception_hierarchy.HierarchyTest()
test_select_error()
