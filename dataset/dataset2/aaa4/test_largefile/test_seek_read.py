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

def test_seek_read():
    with TestFileMethods.open(TESTFN, 'rb') as f:
        TestFileMethods.assertEqual(f.tell(), 0)
        TestFileMethods.assertEqual(f.read(1), b'z')
        TestFileMethods.assertEqual(f.tell(), 1)
        f.seek(0)
        TestFileMethods.assertEqual(f.tell(), 0)
        f.seek(0, 0)
        TestFileMethods.assertEqual(f.tell(), 0)
        f.seek(42)
        TestFileMethods.assertEqual(f.tell(), 42)
        f.seek(42, 0)
        TestFileMethods.assertEqual(f.tell(), 42)
        f.seek(42, 1)
        TestFileMethods.assertEqual(f.tell(), 84)
        f.seek(0, 1)
        TestFileMethods.assertEqual(f.tell(), 84)
        f.seek(0, 2)
        TestFileMethods.assertEqual(f.tell(), size + 1 + 0)
        f.seek(-10, 2)
        TestFileMethods.assertEqual(f.tell(), size + 1 - 10)
        f.seek(-size - 1, 2)
        TestFileMethods.assertEqual(f.tell(), 0)
        f.seek(size)
        TestFileMethods.assertEqual(f.tell(), size)
        TestFileMethods.assertEqual(f.read(1), b'a')
        f.seek(-size - 1, 1)
        TestFileMethods.assertEqual(f.read(1), b'z')
        TestFileMethods.assertEqual(f.tell(), 1)

TestFileMethods = test_largefile.TestFileMethods()
test_seek_read()
