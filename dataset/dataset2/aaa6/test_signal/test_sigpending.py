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
@unittest.skipUnless(hasattr(signal, 'sigpending'), 'need signal.sigpending()')
def test_sigpending():
    code = 'if 1:\n            import os\n            import signal\n\n            def handler(signum, frame):\n                1/0\n\n            signum = signal.SIGUSR1\n            signal.signal(signum, handler)\n\n            signal.pthread_sigmask(signal.SIG_BLOCK, [signum])\n            os.kill(os.getpid(), signum)\n            pending = signal.sigpending()\n            for sig in pending:\n                assert isinstance(sig, signal.Signals), repr(pending)\n            if pending != {signum}:\n                raise Exception(\'%s != {%s}\' % (pending, signum))\n            try:\n                signal.pthread_sigmask(signal.SIG_UNBLOCK, [signum])\n            except ZeroDivisionError:\n                pass\n            else:\n                raise Exception("ZeroDivisionError not raised")\n        '
    assert_python_ok('-c', code)

PendingSignalsTests = test_signal.PendingSignalsTests()
test_sigpending()
