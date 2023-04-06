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

def test_osstat():
    TestFileMethods.assertEqual(os.stat(TESTFN)[stat.ST_SIZE], size + 1)

TestFileMethods = test_largefile.TestFileMethods()
TestFileMethods.setUp()
test_osstat()
