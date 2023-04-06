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

def test_parsing_error():
    args = [sys.executable, '-I', '--unknown-option']
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    err_msg = 'unknown option --unknown-option\nusage: '
    CmdLineTest.assertTrue(proc.stderr.startswith(err_msg), proc.stderr)
    CmdLineTest.assertNotEqual(proc.returncode, 0)

CmdLineTest = test_cmd_line.CmdLineTest()
test_parsing_error()
