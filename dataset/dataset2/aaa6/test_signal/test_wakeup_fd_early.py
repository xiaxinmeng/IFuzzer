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

def test_wakeup_fd_early():
    WakeupSignalTests.check_wakeup('def test():\n            import select\n            import time\n\n            TIMEOUT_FULL = 10\n            TIMEOUT_HALF = 5\n\n            class InterruptSelect(Exception):\n                pass\n\n            def handler(signum, frame):\n                raise InterruptSelect\n            signal.signal(signal.SIGALRM, handler)\n\n            signal.alarm(1)\n\n            # We attempt to get a signal during the sleep,\n            # before select is called\n            try:\n                select.select([], [], [], TIMEOUT_FULL)\n            except InterruptSelect:\n                pass\n            else:\n                raise Exception("select() was not interrupted")\n\n            before_time = time.monotonic()\n            select.select([read], [], [], TIMEOUT_FULL)\n            after_time = time.monotonic()\n            dt = after_time - before_time\n            if dt >= TIMEOUT_HALF:\n                raise Exception("%s >= %s" % (dt, TIMEOUT_HALF))\n        ', signal.SIGALRM)

WakeupSignalTests = test_signal.WakeupSignalTests()
test_wakeup_fd_early()
