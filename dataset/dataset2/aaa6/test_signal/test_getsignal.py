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

def test_getsignal():
    hup = signal.signal(signal.SIGHUP, PosixTests.trivial_signal_handler)
    PosixTests.assertIsInstance(hup, signal.Handlers)
    PosixTests.assertEqual(signal.getsignal(signal.SIGHUP), PosixTests.trivial_signal_handler)
    signal.signal(signal.SIGHUP, hup)
    PosixTests.assertEqual(signal.getsignal(signal.SIGHUP), hup)

PosixTests = test_signal.PosixTests()
test_getsignal()
