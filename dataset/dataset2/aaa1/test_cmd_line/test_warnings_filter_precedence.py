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

def test_warnings_filter_precedence():
    expected_filters = 'error::BytesWarning once::UserWarning always::UserWarning'
    if not test_cmd_line.Py_DEBUG:
        expected_filters += ' default::DeprecationWarning ignore::DeprecationWarning ignore::PendingDeprecationWarning ignore::ImportWarning ignore::ResourceWarning'
    out = CmdLineTest.check_warnings_filters('once::UserWarning', 'always::UserWarning')
    CmdLineTest.assertEqual(out, expected_filters)
    out = CmdLineTest.check_warnings_filters('once::UserWarning', 'always::UserWarning', use_pywarning=True)
    CmdLineTest.assertEqual(out, expected_filters)

CmdLineTest = test_cmd_line.CmdLineTest()
test_warnings_filter_precedence()
