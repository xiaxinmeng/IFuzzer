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

def test_main_thread_during_shutdown():
    code = 'if 1:\n            import gc, threading\n\n            main_thread = threading.current_thread()\n            assert main_thread is threading.main_thread()  # sanity check\n\n            class RefCycle:\n                def __init__(ThreadTests):\n                    ThreadTests.cycle = ThreadTests\n\n                def __del__(ThreadTests):\n                    print("GC:",\n                          threading.current_thread() is main_thread,\n                          threading.main_thread() is main_thread,\n                          threading.enumerate() == [main_thread])\n\n            RefCycle()\n            gc.collect()  # sanity check\n            x = RefCycle()\n        '
    (_, out, err) = assert_python_ok('-c', code)
    data = out.decode()
    ThreadTests.assertEqual(err, b'')
    ThreadTests.assertEqual(data.splitlines(), ['GC: True True True'] * 2)

ThreadTests = test_threading.ThreadTests()
test_main_thread_during_shutdown()
