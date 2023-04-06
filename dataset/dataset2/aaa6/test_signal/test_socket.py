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

@unittest.skipIf(_testcapi is None, 'need _testcapi')
def test_socket():
    code = 'if 1:\n        import signal\n        import socket\n        import struct\n        import _testcapi\n\n        signum = signal.SIGINT\n        signals = (signum,)\n\n        def handler(signum, frame):\n            pass\n\n        signal.signal(signum, handler)\n\n        read, write = socket.socketpair()\n        write.setblocking(False)\n        signal.set_wakeup_fd(write.fileno())\n\n        signal.raise_signal(signum)\n\n        data = read.recv(1)\n        if not data:\n            raise Exception("no signum written")\n        raised = struct.unpack(\'B\', data)\n        if raised != signals:\n            raise Exception("%r != %r" % (raised, signals))\n\n        read.close()\n        write.close()\n        '
    assert_python_ok('-c', code)

WakeupSocketSignalTests = test_signal.WakeupSocketSignalTests()
test_socket()
