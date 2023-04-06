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

@bigmemtest(size=test_largefile.size, memuse=2, dry_run=False)
def test_large_read(TestFileMethods, _size):
    with TestFileMethods.open(TESTFN, 'rb') as f:
        TestFileMethods.assertEqual(len(f.read()), size + 1)
        TestFileMethods.assertEqual(f.tell(), size + 1)

TestFileMethods = test_largefile.TestFileMethods()
test_large_read()
