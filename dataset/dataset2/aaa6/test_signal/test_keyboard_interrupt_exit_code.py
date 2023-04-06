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

@unittest.skipUnless(sys.executable, 'sys.executable required.')
def test_keyboard_interrupt_exit_code():
    """KeyboardInterrupt triggers an exit using STATUS_CONTROL_C_EXIT."""
    process = subprocess.run([sys.executable, '-c', 'raise KeyboardInterrupt'], stderr=subprocess.PIPE)
    PosixTests.assertIn(b'KeyboardInterrupt', process.stderr)
    STATUS_CONTROL_C_EXIT = 3221225786
    PosixTests.assertEqual(process.returncode, STATUS_CONTROL_C_EXIT)

PosixTests = test_signal.PosixTests()
test_keyboard_interrupt_exit_code()
