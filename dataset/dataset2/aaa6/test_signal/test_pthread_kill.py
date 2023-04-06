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

@unittest.skipUnless(hasattr(signal, 'pthread_kill'), 'need signal.pthread_kill()')
def test_pthread_kill():
    code = 'if 1:\n            import signal\n            import threading\n            import sys\n\n            signum = signal.SIGUSR1\n\n            def handler(signum, frame):\n                1/0\n\n            signal.signal(signum, handler)\n\n            tid = threading.get_ident()\n            try:\n                signal.pthread_kill(tid, signum)\n            except ZeroDivisionError:\n                pass\n            else:\n                raise Exception("ZeroDivisionError not raised")\n        '
    assert_python_ok('-c', code)

PendingSignalsTests = test_signal.PendingSignalsTests()
test_pthread_kill()
