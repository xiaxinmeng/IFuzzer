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

@unittest.skipUnless(hasattr(signal, 'sigwaitinfo'), 'need signal.sigwaitinfo()')
def test_sigwaitinfo():
    PendingSignalsTests.wait_helper(signal.SIGALRM, '\n        def test(signum):\n            signal.alarm(1)\n            info = signal.sigwaitinfo([signum])\n            if info.si_signo != signum:\n                raise Exception("info.si_signo != %s" % signum)\n        ')

PendingSignalsTests = test_signal.PendingSignalsTests()
test_sigwaitinfo()
