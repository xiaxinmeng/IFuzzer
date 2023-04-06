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
@unittest.skipUnless(hasattr(signal, 'pthread_sigmask'), 'need signal.pthread_sigmask()')
def test_sigwait_thread():
    assert_python_ok('-c', 'if True:\n            import os, threading, sys, time, signal\n\n            # the default handler terminates the process\n            signum = signal.SIGUSR1\n\n            def kill_later():\n                # wait until the main thread is waiting in sigwait()\n                time.sleep(1)\n                os.kill(os.getpid(), signum)\n\n            # the signal must be blocked by all the threads\n            signal.pthread_sigmask(signal.SIG_BLOCK, [signum])\n            killer = threading.Thread(target=kill_later)\n            killer.start()\n            received = signal.sigwait([signum])\n            if received != signum:\n                print("sigwait() received %s, not %s" % (received, signum),\n                      file=sys.stderr)\n                sys.exit(1)\n            killer.join()\n            # unblock the signal, which should have been cleared by sigwait()\n            signal.pthread_sigmask(signal.SIG_UNBLOCK, [signum])\n        ')

PendingSignalsTests = test_signal.PendingSignalsTests()
test_sigwait_thread()
