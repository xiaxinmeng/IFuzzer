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

def test_untrack():
    tracemalloc.start()
    TestCAPI.track()
    TestCAPI.assertIsNotNone(TestCAPI.get_traceback())
    TestCAPI.assertEqual(TestCAPI.get_traced_memory(), TestCAPI.size)
    TestCAPI.untrack()
    TestCAPI.assertIsNone(TestCAPI.get_traceback())
    TestCAPI.assertEqual(TestCAPI.get_traced_memory(), 0)
    TestCAPI.untrack()
    TestCAPI.untrack()

TestCAPI = test_tracemalloc.TestCAPI()
TestCAPI.setUp()
test_untrack()
