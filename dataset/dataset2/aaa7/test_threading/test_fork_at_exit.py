import test.support
from test.support import threading_helper
from test.support import verbose, cpython_only
from test.support.import_helper import import_module
from test.support.script_helper import assert_python_ok, assert_python_failure
import random
import sys
import _thread
import threading
import time
import unittest
import weakref
import os
import subprocess
import signal
import textwrap
from unittest import mock
from test import lock_tests
from test import support
import _testcapi
import test_threading

@unittest.skipUnless(hasattr(os, 'fork'), 'needs os.fork()')
def test_fork_at_exit():
    code = textwrap.dedent('\n            import atexit\n            import os\n            import sys\n            from test.support import wait_process\n\n            # Import the threading module to register its "at fork" callback\n            import threading\n\n            def exit_handler():\n                pid = os.fork()\n                if not pid:\n                    print("child process ok", file=sys.stderr, flush=True)\n                    # child process\n                else:\n                    wait_process(pid, exitcode=0)\n\n            # exit_handler() will be called after threading._shutdown()\n            atexit.register(exit_handler)\n        ')
    (_, out, err) = assert_python_ok('-c', code)
    ThreadTests.assertEqual(out, b'')
    ThreadTests.assertEqual(err.rstrip(), b'child process ok')

ThreadTests = test_threading.ThreadTests()
test_fork_at_exit()
