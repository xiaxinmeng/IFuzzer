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

def test_env_var_invalid():
    for nframe in test_tracemalloc.INVALID_NFRAME:
        with TestCommandLine.subTest(nframe=nframe):
            TestCommandLine.check_env_var_invalid(nframe)

TestCommandLine = test_tracemalloc.TestCommandLine()
test_env_var_invalid()
