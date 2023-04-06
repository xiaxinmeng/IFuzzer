import platform
import os
import struct
import sys
import unittest
from multiprocessing import Process
from test.support import verbose, run_unittest, cpython_only
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink
from _testcapi import INT_MAX, INT_MIN
import _testcapi
import test_fcntl

@unittest.skipIf(sys.platform != 'darwin', 'F_GETPATH is only available on macos')
def test_fcntl_f_getpath():
    TestFcntl.f = open(TESTFN, 'wb')
    expected = os.path.abspath(TESTFN).encode('utf-8')
    res = test_fcntl.fcntl.fcntl(TestFcntl.f.fileno(), test_fcntl.fcntl.F_GETPATH, bytes(len(expected)))
    TestFcntl.assertEqual(expected, res)

TestFcntl = test_fcntl.TestFcntl()
test_fcntl_f_getpath()
