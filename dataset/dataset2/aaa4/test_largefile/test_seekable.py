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

def test_seekable():
    for pos in (2 ** 31 - 1, 2 ** 31, 2 ** 31 + 1):
        with TestFileMethods.open(TESTFN, 'rb') as f:
            f.seek(pos)
            TestFileMethods.assertTrue(f.seekable())

TestFileMethods = test_largefile.TestFileMethods()
test_seekable()
