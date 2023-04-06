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

def test_handler():
    is_ok = False

    def handler(a, b):
        nonlocal is_ok
        is_ok = True
    old_signal = signal.signal(signal.SIGINT, handler)
    RaiseSignalTest.addCleanup(signal.signal, signal.SIGINT, old_signal)
    signal.raise_signal(signal.SIGINT)
    RaiseSignalTest.assertTrue(is_ok)

RaiseSignalTest = test_signal.RaiseSignalTest()
test_handler()
