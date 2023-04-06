import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import spawn_python, kill_python, assert_python_ok, assert_python_failure, interpreter_requires_environment
import _testcapi
import faulthandler
import test_cmd_line

def test_sys_flags_not_set():
    expected_outcome = '\n            (sys.flags.debug == sys.flags.optimize ==\n             sys.flags.dont_write_bytecode == sys.flags.verbose == 0)\n        '
    IgnoreEnvironmentTest.run_ignoring_vars(expected_outcome, PYTHONDEBUG='1', PYTHONOPTIMIZE='1', PYTHONDONTWRITEBYTECODE='1', PYTHONVERBOSE='1')

IgnoreEnvironmentTest = test_cmd_line.IgnoreEnvironmentTest()
test_sys_flags_not_set()
