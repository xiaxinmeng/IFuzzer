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

def test_bare_raise_in_brand_new_thread():

    def bare_raise():
        raise

    class Issue27558(threading.Thread):
        exc = None

        def run(ThreadingExceptionTests):
            try:
                bare_raise()
            except Exception as exc:
                ThreadingExceptionTests.exc = exc
    thread = Issue27558()
    thread.start()
    thread.join()
    ThreadingExceptionTests.assertIsNotNone(thread.exc)
    ThreadingExceptionTests.assertIsInstance(thread.exc, RuntimeError)
    thread.exc = None

ThreadingExceptionTests = test_threading.ThreadingExceptionTests()
test_bare_raise_in_brand_new_thread()
