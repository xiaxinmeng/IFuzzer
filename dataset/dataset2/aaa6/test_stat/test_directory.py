import unittest
import os
import socket
import sys
from test.support import os_helper
from test.support import socket_helper
from test.support.import_helper import import_fresh_module
from test.support.os_helper import TESTFN
import test_stat

def test_directory():
    os.mkdir(TESTFN)
    os.chmod(TESTFN, 448)
    (st_mode, modestr) = TestFilemode.get_mode()
    TestFilemode.assertS_IS('DIR', st_mode)
    if os.name == 'posix':
        TestFilemode.assertEqual(modestr, 'drwx------')
    else:
        TestFilemode.assertEqual(modestr[0], 'd')

TestFilemode = test_stat.TestFilemode()
test_directory()
