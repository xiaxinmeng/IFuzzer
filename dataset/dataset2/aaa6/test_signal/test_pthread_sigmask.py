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
def test_pthread_sigmask():
    code = 'if 1:\n        import signal\n        import os; import threading\n\n        def handler(signum, frame):\n            1/0\n\n        def kill(signum):\n            os.kill(os.getpid(), signum)\n\n        def check_mask(mask):\n            for sig in mask:\n                assert isinstance(sig, signal.Signals), repr(sig)\n\n        def read_sigmask():\n            sigmask = signal.pthread_sigmask(signal.SIG_BLOCK, [])\n            check_mask(sigmask)\n            return sigmask\n\n        signum = signal.SIGUSR1\n\n        # Install our signal handler\n        old_handler = signal.signal(signum, handler)\n\n        # Unblock SIGUSR1 (and copy the old mask) to test our signal handler\n        old_mask = signal.pthread_sigmask(signal.SIG_UNBLOCK, [signum])\n        check_mask(old_mask)\n        try:\n            kill(signum)\n        except ZeroDivisionError:\n            pass\n        else:\n            raise Exception("ZeroDivisionError not raised")\n\n        # Block and then raise SIGUSR1. The signal is blocked: the signal\n        # handler is not called, and the signal is now pending\n        mask = signal.pthread_sigmask(signal.SIG_BLOCK, [signum])\n        check_mask(mask)\n        kill(signum)\n\n        # Check the new mask\n        blocked = read_sigmask()\n        check_mask(blocked)\n        if signum not in blocked:\n            raise Exception("%s not in %s" % (signum, blocked))\n        if old_mask ^ blocked != {signum}:\n            raise Exception("%s ^ %s != {%s}" % (old_mask, blocked, signum))\n\n        # Unblock SIGUSR1\n        try:\n            # unblock the pending signal calls immediately the signal handler\n            signal.pthread_sigmask(signal.SIG_UNBLOCK, [signum])\n        except ZeroDivisionError:\n            pass\n        else:\n            raise Exception("ZeroDivisionError not raised")\n        try:\n            kill(signum)\n        except ZeroDivisionError:\n            pass\n        else:\n            raise Exception("ZeroDivisionError not raised")\n\n        # Check the new mask\n        unblocked = read_sigmask()\n        if signum in unblocked:\n            raise Exception("%s in %s" % (signum, unblocked))\n        if blocked ^ unblocked != {signum}:\n            raise Exception("%s ^ %s != {%s}" % (blocked, unblocked, signum))\n        if old_mask != unblocked:\n            raise Exception("%s != %s" % (old_mask, unblocked))\n        '
    assert_python_ok('-c', code)

PendingSignalsTests = test_signal.PendingSignalsTests()
test_pthread_sigmask()
