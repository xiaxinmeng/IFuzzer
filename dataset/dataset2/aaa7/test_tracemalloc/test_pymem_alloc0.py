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

@unittest.skipIf(_testcapi is None, 'need _testcapi')
def test_pymem_alloc0():
    code = 'import _testcapi; _testcapi.test_pymem_alloc0(); 1'
    assert_python_ok('-X', 'tracemalloc', '-c', code)

TestCommandLine = test_tracemalloc.TestCommandLine()
test_pymem_alloc0()
