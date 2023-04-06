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

def test_run_module():
    assert_python_failure('-m')
    assert_python_failure('-m', 'fnord43520xyz')
    assert_python_failure('-m', 'runpy', 'fnord43520xyz')
    assert_python_ok('-m', 'timeit', '-n', '1')

CmdLineTest = test_cmd_line.CmdLineTest()
test_run_module()
