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
def test_pending():
    WakeupSignalTests.check_wakeup('def test():\n            signum1 = signal.SIGUSR1\n            signum2 = signal.SIGUSR2\n\n            signal.signal(signum1, handler)\n            signal.signal(signum2, handler)\n\n            signal.pthread_sigmask(signal.SIG_BLOCK, (signum1, signum2))\n            signal.raise_signal(signum1)\n            signal.raise_signal(signum2)\n            # Unblocking the 2 signals calls the C signal handler twice\n            signal.pthread_sigmask(signal.SIG_UNBLOCK, (signum1, signum2))\n        ', signal.SIGUSR1, signal.SIGUSR2, ordered=False)

WakeupSignalTests = test_signal.WakeupSignalTests()
test_pending()
