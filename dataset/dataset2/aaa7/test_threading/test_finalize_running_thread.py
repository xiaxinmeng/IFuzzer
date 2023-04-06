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

def test_finalize_running_thread():
    import_module('ctypes')
    (rc, out, err) = assert_python_failure('-c', 'if 1:\n            import ctypes, sys, time, _thread\n\n            # This lock is used as a simple event variable.\n            ready = _thread.allocate_lock()\n            ready.acquire()\n\n            # Module globals are cleared before __del__ is run\n            # So we save the functions in class dict\n            class C:\n                ensure = ctypes.pythonapi.PyGILState_Ensure\n                release = ctypes.pythonapi.PyGILState_Release\n                def __del__(ThreadTests):\n                    state = ThreadTests.ensure()\n                    ThreadTests.release(state)\n\n            def waitingThread():\n                x = C()\n                ready.release()\n                time.sleep(100)\n\n            _thread.start_new_thread(waitingThread, ())\n            ready.acquire()  # Be sure the other thread is waiting.\n            sys.exit(42)\n            ')
    ThreadTests.assertEqual(rc, 42)

ThreadTests = test_threading.ThreadTests()
test_finalize_running_thread()
