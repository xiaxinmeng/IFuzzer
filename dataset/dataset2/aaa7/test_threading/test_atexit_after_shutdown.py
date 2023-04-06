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

def test_atexit_after_shutdown():
    (rc, out, err) = assert_python_ok('-c', 'if True:\n            import threading\n\n            def func():\n                pass\n\n            def run_last():\n                threading._register_atexit(func)\n\n            threading._register_atexit(run_last)\n        ')
    AtexitTests.assertTrue(err)
    AtexitTests.assertIn("RuntimeError: can't register atexit after shutdown", err.decode())

AtexitTests = test_threading.AtexitTests()
test_atexit_after_shutdown()
