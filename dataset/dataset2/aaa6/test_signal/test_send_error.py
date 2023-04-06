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
def test_send_error():
    if os.name == 'nt':
        action = 'send'
    else:
        action = 'write'
    code = "if 1:\n        import errno\n        import signal\n        import socket\n        import sys\n        import time\n        import _testcapi\n        from test.support import captured_stderr\n\n        signum = signal.SIGINT\n\n        def handler(signum, frame):\n            pass\n\n        signal.signal(signum, handler)\n\n        read, write = socket.socketpair()\n        read.setblocking(False)\n        write.setblocking(False)\n\n        signal.set_wakeup_fd(write.fileno())\n\n        # Close sockets: send() will fail\n        read.close()\n        write.close()\n\n        with captured_stderr() as err:\n            signal.raise_signal(signum)\n\n        err = err.getvalue()\n        if ('Exception ignored when trying to {action} to the signal wakeup fd'\n            not in err):\n            raise AssertionError(err)\n        ".format(action=action)
    assert_python_ok('-c', code)

WakeupSocketSignalTests = test_signal.WakeupSocketSignalTests()
test_send_error()
