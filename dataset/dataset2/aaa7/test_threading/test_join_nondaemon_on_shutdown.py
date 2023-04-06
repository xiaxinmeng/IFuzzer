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

def test_join_nondaemon_on_shutdown():
    (rc, out, err) = assert_python_ok('-c', 'if 1:\n                import threading\n                from time import sleep\n\n                def child():\n                    sleep(1)\n                    # As a non-daemon thread we SHOULD wake up and nothing\n                    # should be torn down yet\n                    print("Woke up, sleep function is:", sleep)\n\n                threading.Thread(target=child).start()\n                raise SystemExit\n            ')
    ThreadTests.assertEqual(out.strip(), b'Woke up, sleep function is: <built-in function sleep>')
    ThreadTests.assertEqual(err, b'')

ThreadTests = test_threading.ThreadTests()
test_join_nondaemon_on_shutdown()
