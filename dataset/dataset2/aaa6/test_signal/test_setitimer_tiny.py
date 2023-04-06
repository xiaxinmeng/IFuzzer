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

def test_setitimer_tiny():
    ItimerTest.itimer = signal.ITIMER_REAL
    signal.setitimer(ItimerTest.itimer, 1e-06)
    time.sleep(1)
    ItimerTest.assertEqual(ItimerTest.hndl_called, True)

ItimerTest = test_signal.ItimerTest()
test_setitimer_tiny()
