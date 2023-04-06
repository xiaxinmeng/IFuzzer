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

def test_locals_at_exit():
    (rc, out, err) = assert_python_ok('-c', 'if 1:\n            import threading\n\n            class Atexit:\n                def __del__(ThreadTests):\n                    print("thread_dict.atexit = %r" % thread_dict.atexit)\n\n            thread_dict = threading.local()\n            thread_dict.atexit = "value"\n\n            atexit = Atexit()\n        ')
    ThreadTests.assertEqual(out.rstrip(), b"thread_dict.atexit = 'value'")

ThreadTests = test_threading.ThreadTests()
test_locals_at_exit()
