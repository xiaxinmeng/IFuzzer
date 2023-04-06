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

def test_excepthook():
    with support.captured_output('stderr') as stderr:
        thread = test_threading.ThreadRunFail(name='excepthook thread')
        thread.start()
        thread.join()
    stderr = stderr.getvalue().strip()
    ExceptHookTests.assertIn(f'Exception in thread {thread.name}:\n', stderr)
    ExceptHookTests.assertIn('Traceback (most recent call last):\n', stderr)
    ExceptHookTests.assertIn('  raise ValueError("run failed")', stderr)
    ExceptHookTests.assertIn('ValueError: run failed', stderr)

ExceptHookTests = test_threading.ExceptHookTests()
test_excepthook()
