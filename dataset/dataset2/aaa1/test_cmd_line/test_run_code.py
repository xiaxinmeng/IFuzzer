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

def test_run_code():
    assert_python_failure('-c')
    assert_python_failure('-c', 'raise Exception')
    assert_python_ok('-c', 'pass')

CmdLineTest = test_cmd_line.CmdLineTest()
test_run_code()
