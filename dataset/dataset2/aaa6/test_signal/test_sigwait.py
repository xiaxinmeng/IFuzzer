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

@unittest.skipUnless(hasattr(signal, 'sigwait'), 'need signal.sigwait()')
def test_sigwait():
    PendingSignalsTests.wait_helper(signal.SIGALRM, "\n        def test(signum):\n            signal.alarm(1)\n            received = signal.sigwait([signum])\n            assert isinstance(received, signal.Signals), received\n            if received != signum:\n                raise Exception('received %s, not %s' % (received, signum))\n        ")

PendingSignalsTests = test_signal.PendingSignalsTests()
test_sigwait()
