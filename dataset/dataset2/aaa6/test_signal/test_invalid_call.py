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

def test_invalid_call():
    with WakeupFDTests.assertRaises(TypeError):
        signal.set_wakeup_fd(signum=signal.SIGINT)
    with WakeupFDTests.assertRaises(TypeError):
        signal.set_wakeup_fd(signal.SIGINT, False)

WakeupFDTests = test_signal.WakeupFDTests()
test_invalid_call()
