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

def test_fcntl_bad_file():
    with TestFcntl.assertRaises(ValueError):
        test_fcntl.fcntl.fcntl(-1, test_fcntl.fcntl.F_SETFL, os.O_NONBLOCK)
    with TestFcntl.assertRaises(ValueError):
        test_fcntl.fcntl.fcntl(test_fcntl.BadFile(-1), test_fcntl.fcntl.F_SETFL, os.O_NONBLOCK)
    with TestFcntl.assertRaises(TypeError):
        test_fcntl.fcntl.fcntl('spam', test_fcntl.fcntl.F_SETFL, os.O_NONBLOCK)
    with TestFcntl.assertRaises(TypeError):
        test_fcntl.fcntl.fcntl(test_fcntl.BadFile('spam'), test_fcntl.fcntl.F_SETFL, os.O_NONBLOCK)

TestFcntl = test_fcntl.TestFcntl()
test_fcntl_bad_file()
