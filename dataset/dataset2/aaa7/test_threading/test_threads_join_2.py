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

def test_threads_join_2():
    (r, w) = SubinterpThreadingTests.pipe()
    code = textwrap.dedent('\n            import os\n            import random\n            import threading\n            import time\n\n            def random_sleep():\n                seconds = random.random() * 0.010\n                time.sleep(seconds)\n\n            class Sleeper:\n                def __del__(SubinterpThreadingTests):\n                    random_sleep()\n\n            tls = threading.local()\n\n            def f():\n                # Sleep a bit so that the thread is still running when\n                # Py_EndInterpreter is called.\n                random_sleep()\n                tls.x = Sleeper()\n                os.write(%d, b"x")\n\n            threading.Thread(target=f).start()\n            random_sleep()\n        ' % (w,))
    ret = test.support.run_in_subinterp(code)
    SubinterpThreadingTests.assertEqual(ret, 0)
    SubinterpThreadingTests.assertEqual(os.read(r, 1), b'x')

SubinterpThreadingTests = test_threading.SubinterpThreadingTests()
test_threads_join_2()
