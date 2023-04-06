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

@unittest.skipIf(platform.system() == 'AIX', 'AIX returns PermissionError')
def test_lockf_share():
    TestFcntl.f = open(TESTFN, 'wb+')
    cmd = test_fcntl.fcntl.LOCK_SH | test_fcntl.fcntl.LOCK_NB
    test_fcntl.fcntl.lockf(TestFcntl.f, cmd)
    p = Process(target=test_fcntl.try_lockf_on_other_process, args=(TESTFN, cmd))
    p.start()
    p.join()
    test_fcntl.fcntl.lockf(TestFcntl.f, test_fcntl.fcntl.LOCK_UN)
    TestFcntl.assertEqual(p.exitcode, 0)

TestFcntl = test_fcntl.TestFcntl()
test_lockf_share()
