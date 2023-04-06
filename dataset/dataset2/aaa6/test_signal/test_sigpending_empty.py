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

@unittest.skipUnless(hasattr(signal, 'sigpending'), 'need signal.sigpending()')
def test_sigpending_empty():
    PendingSignalsTests.assertEqual(signal.sigpending(), set())

PendingSignalsTests = test_signal.PendingSignalsTests()
test_sigpending_empty()
