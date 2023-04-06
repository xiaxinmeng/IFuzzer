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

def test_limbo_cleanup():

    def fail_new_thread(*args):
        raise threading.ThreadError()
    _start_new_thread = threading._start_new_thread
    threading._start_new_thread = fail_new_thread
    try:
        t = threading.Thread(target=lambda : None)
        ThreadTests.assertRaises(threading.ThreadError, t.start)
        ThreadTests.assertFalse(t in threading._limbo, 'Failed to cleanup _limbo map on failure of Thread.start().')
    finally:
        threading._start_new_thread = _start_new_thread

ThreadTests = test_threading.ThreadTests()
test_limbo_cleanup()
