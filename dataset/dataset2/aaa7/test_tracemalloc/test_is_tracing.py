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

def test_is_tracing():
    tracemalloc.stop()
    TestTracemallocEnabled.assertFalse(tracemalloc.is_tracing())
    tracemalloc.start()
    TestTracemallocEnabled.assertTrue(tracemalloc.is_tracing())

TestTracemallocEnabled = test_tracemalloc.TestTracemallocEnabled()
test_is_tracing()
