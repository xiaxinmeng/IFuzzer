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

def test_snapshot():
    (obj, source) = test_tracemalloc.allocate_bytes(123)
    snapshot = tracemalloc.take_snapshot()
    TestTracemallocEnabled.assertGreater(snapshot.traces[1].traceback.total_nframe, 10)
    snapshot.dump(os_helper.TESTFN)
    TestTracemallocEnabled.addCleanup(os_helper.unlink, os_helper.TESTFN)
    snapshot2 = tracemalloc.Snapshot.load(os_helper.TESTFN)
    TestTracemallocEnabled.assertEqual(snapshot2.traces, snapshot.traces)
    tracemalloc.stop()
    with TestTracemallocEnabled.assertRaises(RuntimeError) as cm:
        tracemalloc.take_snapshot()
    TestTracemallocEnabled.assertEqual(str(cm.exception), 'the tracemalloc module must be tracing memory allocations to take a snapshot')

TestTracemallocEnabled = test_tracemalloc.TestTracemallocEnabled()
test_snapshot()
