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

def test_itimer_prof():
    ItimerTest.itimer = signal.ITIMER_PROF
    signal.signal(signal.SIGPROF, ItimerTest.sig_prof)
    signal.setitimer(ItimerTest.itimer, 0.2, 0.2)
    start_time = time.monotonic()
    while time.monotonic() - start_time < 60.0:
        _ = pow(12345, 67890, 10000019)
        if signal.getitimer(ItimerTest.itimer) == (0.0, 0.0):
            break
    else:
        ItimerTest.skipTest('timeout: likely cause: machine too slow or load too high')
    ItimerTest.assertEqual(signal.getitimer(ItimerTest.itimer), (0.0, 0.0))
    ItimerTest.assertEqual(ItimerTest.hndl_called, True)

ItimerTest = test_signal.ItimerTest()
test_itimer_prof()
