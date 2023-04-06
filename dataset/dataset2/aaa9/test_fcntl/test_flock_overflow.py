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

@cpython_only
def test_flock_overflow():
    import _testcapi
    TestFcntl.assertRaises(OverflowError, test_fcntl.fcntl.flock, _testcapi.INT_MAX + 1, test_fcntl.fcntl.LOCK_SH)

TestFcntl = test_fcntl.TestFcntl()
test_flock_overflow()
