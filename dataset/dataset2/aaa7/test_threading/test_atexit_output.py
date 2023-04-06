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

def test_atexit_output():
    (rc, out, err) = assert_python_ok('-c', "if True:\n            import threading\n\n            def run_last():\n                print('parrot')\n\n            threading._register_atexit(run_last)\n        ")
    AtexitTests.assertFalse(err)
    AtexitTests.assertEqual(out.strip(), b'parrot')

AtexitTests = test_threading.AtexitTests()
test_atexit_output()
