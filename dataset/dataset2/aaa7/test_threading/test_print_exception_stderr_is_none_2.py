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

def test_print_exception_stderr_is_none_2():
    script = 'if True:\n            import sys\n            import threading\n            import time\n\n            running = False\n            def run():\n                global running\n                running = True\n                while running:\n                    time.sleep(0.01)\n                1/0\n            sys.stderr = None\n            t = threading.Thread(target=run)\n            t.start()\n            while not running:\n                time.sleep(0.01)\n            running = False\n            t.join()\n            '
    (rc, out, err) = assert_python_ok('-c', script)
    ThreadingExceptionTests.assertEqual(out, b'')
    ThreadingExceptionTests.assertNotIn('Unhandled exception', err.decode())

ThreadingExceptionTests = test_threading.ThreadingExceptionTests()
test_print_exception_stderr_is_none_2()
