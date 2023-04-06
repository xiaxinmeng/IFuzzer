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
def test_warn_on_full_buffer():
    if os.name == 'nt':
        action = 'send'
    else:
        action = 'write'
    code = 'if 1:\n        import errno\n        import signal\n        import socket\n        import sys\n        import time\n        import _testcapi\n        from test.support import captured_stderr\n\n        signum = signal.SIGINT\n\n        # This handler will be called, but we intentionally won\'t read from\n        # the wakeup fd.\n        def handler(signum, frame):\n            pass\n\n        signal.signal(signum, handler)\n\n        read, write = socket.socketpair()\n\n        # Fill the socketpair buffer\n        if sys.platform == \'win32\':\n            # bpo-34130: On Windows, sometimes non-blocking send fails to fill\n            # the full socketpair buffer, so use a timeout of 50 ms instead.\n            write.settimeout(0.050)\n        else:\n            write.setblocking(False)\n\n        written = 0\n        if sys.platform == "vxworks":\n            CHUNK_SIZES = (1,)\n        else:\n            # Start with large chunk size to reduce the\n            # number of send needed to fill the buffer.\n            CHUNK_SIZES = (2 ** 16, 2 ** 8, 1)\n        for chunk_size in CHUNK_SIZES:\n            chunk = b"x" * chunk_size\n            try:\n                while True:\n                    write.send(chunk)\n                    written += chunk_size\n            except (BlockingIOError, TimeoutError):\n                pass\n\n        print(f"%s bytes written into the socketpair" % written, flush=True)\n\n        write.setblocking(False)\n        try:\n            write.send(b"x")\n        except BlockingIOError:\n            # The socketpair buffer seems full\n            pass\n        else:\n            raise AssertionError("%s bytes failed to fill the socketpair "\n                                 "buffer" % written)\n\n        # By default, we get a warning when a signal arrives\n        msg = (\'Exception ignored when trying to {action} \'\n               \'to the signal wakeup fd\')\n        signal.set_wakeup_fd(write.fileno())\n\n        with captured_stderr() as err:\n            signal.raise_signal(signum)\n\n        err = err.getvalue()\n        if msg not in err:\n            raise AssertionError("first set_wakeup_fd() test failed, "\n                                 "stderr: %r" % err)\n\n        # And also if warn_on_full_buffer=True\n        signal.set_wakeup_fd(write.fileno(), warn_on_full_buffer=True)\n\n        with captured_stderr() as err:\n            signal.raise_signal(signum)\n\n        err = err.getvalue()\n        if msg not in err:\n            raise AssertionError("set_wakeup_fd(warn_on_full_buffer=True) "\n                                 "test failed, stderr: %r" % err)\n\n        # But not if warn_on_full_buffer=False\n        signal.set_wakeup_fd(write.fileno(), warn_on_full_buffer=False)\n\n        with captured_stderr() as err:\n            signal.raise_signal(signum)\n\n        err = err.getvalue()\n        if err != "":\n            raise AssertionError("set_wakeup_fd(warn_on_full_buffer=False) "\n                                 "test failed, stderr: %r" % err)\n\n        # And then check the default again, to make sure warn_on_full_buffer\n        # settings don\'t leak across calls.\n        signal.set_wakeup_fd(write.fileno())\n\n        with captured_stderr() as err:\n            signal.raise_signal(signum)\n\n        err = err.getvalue()\n        if msg not in err:\n            raise AssertionError("second set_wakeup_fd() test failed, "\n                                 "stderr: %r" % err)\n\n        '.format(action=action)
    assert_python_ok('-c', code)

WakeupSocketSignalTests = test_signal.WakeupSocketSignalTests()
test_warn_on_full_buffer()
