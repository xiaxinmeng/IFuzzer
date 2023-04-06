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

def test_env_limit():
    code = 'import tracemalloc; print(tracemalloc.get_traceback_limit())'
    (ok, stdout, stderr) = assert_python_ok('-c', code, PYTHONTRACEMALLOC='10')
    stdout = stdout.rstrip()
    TestCommandLine.assertEqual(stdout, b'10')

TestCommandLine = test_tracemalloc.TestCommandLine()
test_env_limit()
