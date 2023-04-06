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

def test_valid_signals():
    s = signal.valid_signals()
    PosixTests.assertIsInstance(s, set)
    PosixTests.assertGreaterEqual(len(s), 6)
    PosixTests.assertIn(signal.Signals.SIGINT, s)
    PosixTests.assertNotIn(0, s)
    PosixTests.assertNotIn(signal.NSIG, s)
    PosixTests.assertLess(len(s), signal.NSIG)

PosixTests = test_signal.PosixTests()
test_valid_signals()
