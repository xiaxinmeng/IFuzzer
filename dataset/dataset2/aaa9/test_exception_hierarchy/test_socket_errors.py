import builtins
import os
import select
import socket
import unittest
import errno
from errno import EEXIST
import test_exception_hierarchy

def test_socket_errors():
    HierarchyTest.assertIs(socket.error, OSError)
    HierarchyTest.assertIs(socket.gaierror.__base__, OSError)
    HierarchyTest.assertIs(socket.herror.__base__, OSError)
    HierarchyTest.assertIs(socket.timeout, TimeoutError)

HierarchyTest = test_exception_hierarchy.HierarchyTest()
test_socket_errors()
