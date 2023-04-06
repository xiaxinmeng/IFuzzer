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

def test_finalize_with_trace():
    assert_python_ok('-c', "if 1:\n            import sys, threading\n\n            # A deadlock-killer, to prevent the\n            # testsuite to hang forever\n            def killer():\n                import os, time\n                time.sleep(2)\n                print('program blocked; aborting')\n                os._exit(2)\n            t = threading.Thread(target=killer)\n            t.daemon = True\n            t.start()\n\n            # This is the trace function\n            def func(frame, event, arg):\n                threading.current_thread()\n                return func\n\n            sys.settrace(func)\n            ")

ThreadTests = test_threading.ThreadTests()
test_finalize_with_trace()
