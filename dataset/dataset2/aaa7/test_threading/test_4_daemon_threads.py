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

@unittest.skipIf(sys.platform in test_threading.platforms_to_skip, 'due to known OS bug')
def test_4_daemon_threads():
    script = "if True:\n            import os\n            import random\n            import sys\n            import time\n            import threading\n\n            thread_has_run = set()\n\n            def random_io():\n                '''Loop for a while sleeping random tiny amounts and doing some I/O.'''\n                while True:\n                    with open(os.__file__, 'rb') as in_f:\n                        stuff = in_f.read(200)\n                        with open(os.devnull, 'wb') as null_f:\n                            null_f.write(stuff)\n                            time.sleep(random.random() / 1995)\n                    thread_has_run.add(threading.current_thread())\n\n            def main():\n                count = 0\n                for _ in range(40):\n                    new_thread = threading.Thread(target=random_io)\n                    new_thread.daemon = True\n                    new_thread.start()\n                    count += 1\n                while len(thread_has_run) < count:\n                    time.sleep(0.001)\n                # Trigger process shutdown\n                sys.exit(0)\n\n            main()\n            "
    (rc, out, err) = assert_python_ok('-c', script)
    ThreadJoinOnShutdown.assertFalse(err)

ThreadJoinOnShutdown = test_threading.ThreadJoinOnShutdown()
test_4_daemon_threads()
