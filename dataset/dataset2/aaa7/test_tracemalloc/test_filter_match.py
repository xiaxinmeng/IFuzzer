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

def test_filter_match():
    f = tracemalloc.Filter(True, 'abc')
    TestFilters.assertTrue(f._match_frame('abc', 0))
    TestFilters.assertTrue(f._match_frame('abc', 5))
    TestFilters.assertTrue(f._match_frame('abc', 10))
    TestFilters.assertFalse(f._match_frame('12356', 0))
    TestFilters.assertFalse(f._match_frame('12356', 5))
    TestFilters.assertFalse(f._match_frame('12356', 10))
    f = tracemalloc.Filter(False, 'abc')
    TestFilters.assertFalse(f._match_frame('abc', 0))
    TestFilters.assertFalse(f._match_frame('abc', 5))
    TestFilters.assertFalse(f._match_frame('abc', 10))
    TestFilters.assertTrue(f._match_frame('12356', 0))
    TestFilters.assertTrue(f._match_frame('12356', 5))
    TestFilters.assertTrue(f._match_frame('12356', 10))
    f = tracemalloc.Filter(True, 'abc', 5)
    TestFilters.assertFalse(f._match_frame('abc', 0))
    TestFilters.assertTrue(f._match_frame('abc', 5))
    TestFilters.assertFalse(f._match_frame('abc', 10))
    TestFilters.assertFalse(f._match_frame('12356', 0))
    TestFilters.assertFalse(f._match_frame('12356', 5))
    TestFilters.assertFalse(f._match_frame('12356', 10))
    f = tracemalloc.Filter(False, 'abc', 5)
    TestFilters.assertTrue(f._match_frame('abc', 0))
    TestFilters.assertFalse(f._match_frame('abc', 5))
    TestFilters.assertTrue(f._match_frame('abc', 10))
    TestFilters.assertTrue(f._match_frame('12356', 0))
    TestFilters.assertTrue(f._match_frame('12356', 5))
    TestFilters.assertTrue(f._match_frame('12356', 10))
    f = tracemalloc.Filter(True, 'abc', 0)
    TestFilters.assertTrue(f._match_frame('abc', 0))
    TestFilters.assertFalse(f._match_frame('abc', 5))
    TestFilters.assertFalse(f._match_frame('abc', 10))
    TestFilters.assertFalse(f._match_frame('12356', 0))
    TestFilters.assertFalse(f._match_frame('12356', 5))
    TestFilters.assertFalse(f._match_frame('12356', 10))
    f = tracemalloc.Filter(False, 'abc', 0)
    TestFilters.assertFalse(f._match_frame('abc', 0))
    TestFilters.assertTrue(f._match_frame('abc', 5))
    TestFilters.assertTrue(f._match_frame('abc', 10))
    TestFilters.assertTrue(f._match_frame('12356', 0))
    TestFilters.assertTrue(f._match_frame('12356', 5))
    TestFilters.assertTrue(f._match_frame('12356', 10))

TestFilters = test_tracemalloc.TestFilters()
test_filter_match()
