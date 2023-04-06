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

def test_snapshot_save_attr():
    snapshot = tracemalloc.take_snapshot()
    snapshot.test_attr = 'new'
    snapshot.dump(os_helper.TESTFN)
    TestTracemallocEnabled.addCleanup(os_helper.unlink, os_helper.TESTFN)
    snapshot2 = tracemalloc.Snapshot.load(os_helper.TESTFN)
    TestTracemallocEnabled.assertEqual(snapshot2.test_attr, 'new')

TestTracemallocEnabled = test_tracemalloc.TestTracemallocEnabled()
test_snapshot_save_attr()
