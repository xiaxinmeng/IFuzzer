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

def test_set_wakeup_fd_socket_result():
    sock1 = socket.socket()
    WakeupFDTests.addCleanup(sock1.close)
    sock1.setblocking(False)
    fd1 = sock1.fileno()
    sock2 = socket.socket()
    WakeupFDTests.addCleanup(sock2.close)
    sock2.setblocking(False)
    fd2 = sock2.fileno()
    signal.set_wakeup_fd(fd1)
    WakeupFDTests.assertEqual(signal.set_wakeup_fd(fd2), fd1)
    WakeupFDTests.assertEqual(signal.set_wakeup_fd(-1), fd2)
    WakeupFDTests.assertEqual(signal.set_wakeup_fd(-1), -1)

WakeupFDTests = test_signal.WakeupFDTests()
test_set_wakeup_fd_socket_result()
