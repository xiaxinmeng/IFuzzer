import unittest
import os
import socket
import sys
from test.support import os_helper
from test.support import socket_helper
from test.support.import_helper import import_fresh_module
from test.support.os_helper import TESTFN
import test_stat

@socket_helper.skip_unless_bind_unix_socket
def test_socket():
    with socket.socket(socket.AF_UNIX) as s:
        s.bind(TESTFN)
        (st_mode, modestr) = TestFilemode.get_mode()
        TestFilemode.assertEqual(modestr[0], 's')
        TestFilemode.assertS_IS('SOCK', st_mode)

TestFilemode = test_stat.TestFilemode()
test_socket()
