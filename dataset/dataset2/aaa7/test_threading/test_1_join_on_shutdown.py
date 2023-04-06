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

def test_1_join_on_shutdown():
    script = "if 1:\n            import os\n            t = threading.Thread(target=joiningfunc,\n                                 args=(threading.current_thread(),))\n            t.start()\n            time.sleep(0.1)\n            print('end of main')\n            "
    ThreadJoinOnShutdown._run_and_join(script)

ThreadJoinOnShutdown = test_threading.ThreadJoinOnShutdown()
test_1_join_on_shutdown()
