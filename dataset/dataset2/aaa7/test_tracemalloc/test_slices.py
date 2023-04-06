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

def test_slices():
    (snapshot, snapshot2) = test_tracemalloc.create_snapshots()
    TestSnapshot.assertEqual(snapshot.traces[:2], (snapshot.traces[0], snapshot.traces[1]))
    traceback = snapshot.traces[0].traceback
    TestSnapshot.assertEqual(traceback[:2], (traceback[0], traceback[1]))

TestSnapshot = test_tracemalloc.TestSnapshot()
test_slices()
