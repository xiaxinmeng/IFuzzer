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

@unittest.skipUnless(hasattr(signal, 'sigtimedwait'), 'need signal.sigtimedwait()')
def test_sigtimedwait_poll():
    PendingSignalsTests.wait_helper(signal.SIGALRM, "\n        def test(signum):\n            import os\n            os.kill(os.getpid(), signum)\n            info = signal.sigtimedwait([signum], 0)\n            if info.si_signo != signum:\n                raise Exception('info.si_signo != %s' % signum)\n        ")

PendingSignalsTests = test_signal.PendingSignalsTests()
test_sigtimedwait_poll()
