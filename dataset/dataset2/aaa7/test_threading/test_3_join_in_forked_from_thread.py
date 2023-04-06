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

@unittest.skipUnless(hasattr(os, 'fork'), 'needs os.fork()')
@unittest.skipIf(sys.platform in test_threading.platforms_to_skip, 'due to known OS bug')
def test_3_join_in_forked_from_thread():
    script = "if 1:\n            from test import support\n\n            main_thread = threading.current_thread()\n            def worker():\n                childpid = os.fork()\n                if childpid != 0:\n                    # parent process\n                    support.wait_process(childpid, exitcode=0)\n                    sys.exit(0)\n\n                # child process\n                t = threading.Thread(target=joiningfunc,\n                                     args=(main_thread,))\n                print('end of main')\n                t.start()\n                t.join() # Should not block: main_thread is already stopped\n\n            w = threading.Thread(target=worker)\n            w.start()\n            "
    ThreadJoinOnShutdown._run_and_join(script)

ThreadJoinOnShutdown = test_threading.ThreadJoinOnShutdown()
test_3_join_in_forked_from_thread()
