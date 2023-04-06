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

def test_env_var_enabled_at_startup():
    code = 'import tracemalloc; print(tracemalloc.is_tracing())'
    (ok, stdout, stderr) = assert_python_ok('-c', code, PYTHONTRACEMALLOC='1')
    stdout = stdout.rstrip()
    TestCommandLine.assertEqual(stdout, b'True')

TestCommandLine = test_tracemalloc.TestCommandLine()
test_env_var_enabled_at_startup()
