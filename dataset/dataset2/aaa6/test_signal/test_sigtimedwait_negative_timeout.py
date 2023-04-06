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
def test_sigtimedwait_negative_timeout():
    signum = signal.SIGALRM
    PendingSignalsTests.assertRaises(ValueError, signal.sigtimedwait, [signum], -1.0)

PendingSignalsTests = test_signal.PendingSignalsTests()
test_sigtimedwait_negative_timeout()
