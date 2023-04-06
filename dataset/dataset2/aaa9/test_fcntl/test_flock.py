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

def test_flock():
    TestFcntl.f = open(TESTFN, 'wb+')
    fileno = TestFcntl.f.fileno()
    test_fcntl.fcntl.flock(fileno, test_fcntl.fcntl.LOCK_SH)
    test_fcntl.fcntl.flock(fileno, test_fcntl.fcntl.LOCK_UN)
    test_fcntl.fcntl.flock(TestFcntl.f, test_fcntl.fcntl.LOCK_SH | test_fcntl.fcntl.LOCK_NB)
    test_fcntl.fcntl.flock(TestFcntl.f, test_fcntl.fcntl.LOCK_UN)
    test_fcntl.fcntl.flock(fileno, test_fcntl.fcntl.LOCK_EX)
    test_fcntl.fcntl.flock(fileno, test_fcntl.fcntl.LOCK_UN)
    TestFcntl.assertRaises(ValueError, test_fcntl.fcntl.flock, -1, test_fcntl.fcntl.LOCK_SH)
    TestFcntl.assertRaises(TypeError, test_fcntl.fcntl.flock, 'spam', test_fcntl.fcntl.LOCK_SH)

TestFcntl = test_fcntl.TestFcntl()
test_flock()
