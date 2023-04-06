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

def test_ignore_PYTHONHASHSEED():
    IgnoreEnvironmentTest.run_ignoring_vars('sys.flags.hash_randomization == 1', PYTHONHASHSEED='0')

IgnoreEnvironmentTest = test_cmd_line.IgnoreEnvironmentTest()
test_ignore_PYTHONHASHSEED()
