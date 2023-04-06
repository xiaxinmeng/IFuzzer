import contextlib
import os
import sys
import tracemalloc
import unittest
from unittest.mock import patch
from test.support.script_helper import assert_python_ok, assert_python_failure, interpreter_requires_environment
from test import support
from test.support import os_helper
import _testcapi
import test_tracemalloc

@unittest.skipUnless(hasattr(os, 'fork'), 'need os.fork()')
def test_fork():
    pid = os.fork()
    if not pid:
        exitcode = 1
        try:
            exitcode = TestTracemallocEnabled.fork_child()
        finally:
            os._exit(exitcode)
    else:
        support.wait_process(pid, exitcode=0)

TestTracemallocEnabled = test_tracemalloc.TestTracemallocEnabled()
test_fork()
