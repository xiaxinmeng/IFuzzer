import os
import stat
import sys
import unittest
import socket
import shutil
import threading
from test.support import requires, bigmemtest
from test.support import SHORT_TIMEOUT
from test.support import socket_helper
from test.support.os_helper import TESTFN, unlink
import io
import _pyio as pyio
import signal
import test_largefile

def test_lseek():
    with TestFileMethods.open(TESTFN, 'rb') as f:
        TestFileMethods.assertEqual(os.lseek(f.fileno(), 0, 0), 0)
        TestFileMethods.assertEqual(os.lseek(f.fileno(), 42, 0), 42)
        TestFileMethods.assertEqual(os.lseek(f.fileno(), 42, 1), 84)
        TestFileMethods.assertEqual(os.lseek(f.fileno(), 0, 1), 84)
        TestFileMethods.assertEqual(os.lseek(f.fileno(), 0, 2), size + 1 + 0)
        TestFileMethods.assertEqual(os.lseek(f.fileno(), -10, 2), size + 1 - 10)
        TestFileMethods.assertEqual(os.lseek(f.fileno(), -size - 1, 2), 0)
        TestFileMethods.assertEqual(os.lseek(f.fileno(), size, 0), size)
        TestFileMethods.assertEqual(f.read(1), b'a')

TestFileMethods = test_largefile.TestFileMethods()
TestFileMethods.setUp()
test_lseek()
