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

def test_ident_of_no_threading_threads():
    ThreadTests.assertIsNotNone(threading.currentThread().ident)

    def f():
        ident.append(threading.currentThread().ident)
        done.set()
    done = threading.Event()
    ident = []
    with threading_helper.wait_threads_exit():
        tid = _thread.start_new_thread(f, ())
        done.wait()
        ThreadTests.assertEqual(ident[0], tid)
    del threading._active[ident[0]]

ThreadTests = test_threading.ThreadTests()
test_ident_of_no_threading_threads()
