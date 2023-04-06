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

@unittest.skipUnless(hasattr(signal, 'pthread_sigmask'), 'need signal.pthread_sigmask()')
def test_pthread_sigmask_valid_signals():
    s = signal.pthread_sigmask(signal.SIG_BLOCK, signal.valid_signals())
    PendingSignalsTests.addCleanup(signal.pthread_sigmask, signal.SIG_SETMASK, s)
    s = signal.pthread_sigmask(signal.SIG_UNBLOCK, signal.valid_signals())
    PendingSignalsTests.assertLessEqual(s, signal.valid_signals())

PendingSignalsTests = test_signal.PendingSignalsTests()
test_pthread_sigmask_valid_signals()
