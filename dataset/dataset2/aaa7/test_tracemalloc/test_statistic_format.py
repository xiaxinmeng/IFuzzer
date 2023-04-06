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

def test_statistic_format():
    (snapshot, snapshot2) = test_tracemalloc.create_snapshots()
    stats = snapshot.statistics('lineno')
    stat = stats[0]
    TestSnapshot.assertEqual(str(stat), 'b.py:1: size=66 B, count=1, average=66 B')

TestSnapshot = test_tracemalloc.TestSnapshot()
test_statistic_format()
