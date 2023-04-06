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

def test_filter_attributes():
    f = tracemalloc.Filter(True, 'abc')
    TestFilters.assertEqual(f.inclusive, True)
    TestFilters.assertEqual(f.filename_pattern, 'abc')
    TestFilters.assertIsNone(f.lineno)
    TestFilters.assertEqual(f.all_frames, False)
    f = tracemalloc.Filter(False, 'test.py', 123, True)
    TestFilters.assertEqual(f.inclusive, False)
    TestFilters.assertEqual(f.filename_pattern, 'test.py')
    TestFilters.assertEqual(f.lineno, 123)
    TestFilters.assertEqual(f.all_frames, True)
    f = tracemalloc.Filter(inclusive=False, filename_pattern='test.py', lineno=123, all_frames=True)
    TestFilters.assertEqual(f.inclusive, False)
    TestFilters.assertEqual(f.filename_pattern, 'test.py')
    TestFilters.assertEqual(f.lineno, 123)
    TestFilters.assertEqual(f.all_frames, True)
    TestFilters.assertRaises(AttributeError, setattr, f, 'filename_pattern', 'abc')

TestFilters = test_tracemalloc.TestFilters()
test_filter_attributes()
