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

def test_tstate_lock():
    started = _thread.allocate_lock()
    finish = _thread.allocate_lock()
    started.acquire()
    finish.acquire()

    def f():
        started.release()
        finish.acquire()
        time.sleep(0.01)
    t = threading.Thread(target=f)
    ThreadTests.assertIs(t._tstate_lock, None)
    t.start()
    started.acquire()
    ThreadTests.assertTrue(t.is_alive())
    tstate_lock = t._tstate_lock
    ThreadTests.assertFalse(tstate_lock.acquire(timeout=0), False)
    finish.release()
    ThreadTests.assertTrue(tstate_lock.acquire(timeout=support.SHORT_TIMEOUT), False)
    ThreadTests.assertTrue(t.is_alive())
    tstate_lock.release()
    ThreadTests.assertFalse(t.is_alive())
    ThreadTests.assertIsNone(t._tstate_lock)
    t.join()

ThreadTests = test_threading.ThreadTests()
test_tstate_lock()
