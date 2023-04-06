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

def test_stop_track():
    tracemalloc.start()
    tracemalloc.stop()
    with TestCAPI.assertRaises(RuntimeError):
        TestCAPI.track()
    TestCAPI.assertIsNone(TestCAPI.get_traceback())

TestCAPI = test_tracemalloc.TestCAPI()
TestCAPI.setUp()
test_stop_track()
