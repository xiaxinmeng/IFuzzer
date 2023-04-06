import errno
import os
import random
import signal
import socket
import statistics
import subprocess
import sys
import time
import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok, spawn_python
import _testcapi
import test_signal

@unittest.skipIf(sys.platform != 'win32', 'Windows specific test')
def test_invalid_argument():
    try:
        SIGHUP = 1
        signal.raise_signal(SIGHUP)
        RaiseSignalTest.fail('OSError (Invalid argument) expected')
    except OSError as e:
        if e.errno == errno.EINVAL:
            pass
        else:
            raise

RaiseSignalTest = test_signal.RaiseSignalTest()
test_invalid_argument()
