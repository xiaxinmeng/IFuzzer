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

def test_signum():
    WakeupSignalTests.check_wakeup('def test():\n            signal.signal(signal.SIGUSR1, handler)\n            signal.raise_signal(signal.SIGUSR1)\n            signal.raise_signal(signal.SIGALRM)\n        ', signal.SIGUSR1, signal.SIGALRM)

WakeupSignalTests = test_signal.WakeupSignalTests()
test_signum()
