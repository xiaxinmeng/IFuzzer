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

def test_statistic_diff_format():
    (snapshot, snapshot2) = test_tracemalloc.create_snapshots()
    stats = snapshot2.compare_to(snapshot, 'lineno')
    stat = stats[0]
    TestSnapshot.assertEqual(str(stat), 'a.py:5: size=5002 B (+5000 B), count=2 (+1), average=2501 B')

TestSnapshot = test_tracemalloc.TestSnapshot()
test_statistic_diff_format()
