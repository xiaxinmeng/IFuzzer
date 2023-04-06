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

def test_fcntl_file_descriptor():
    TestFcntl.f = open(TESTFN, 'wb')
    rv = test_fcntl.fcntl.fcntl(TestFcntl.f, test_fcntl.fcntl.F_SETFL, os.O_NONBLOCK)
    if verbose:
        print('Status from fcntl with O_NONBLOCK: ', rv)
    rv = test_fcntl.fcntl.fcntl(TestFcntl.f, test_fcntl.fcntl.F_SETLKW, test_fcntl.lockdata)
    if verbose:
        print('String from fcntl with F_SETLKW: ', repr(rv))
    TestFcntl.f.close()

TestFcntl = test_fcntl.TestFcntl()
test_fcntl_file_descriptor()
