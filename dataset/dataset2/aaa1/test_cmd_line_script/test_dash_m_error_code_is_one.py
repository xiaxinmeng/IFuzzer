import contextlib
import importlib
import importlib.machinery
import zipimport
import unittest
import sys
import os
import os.path
import py_compile
import subprocess
import io
import textwrap
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support.script_helper import make_pkg, make_script, make_zip_pkg, make_zip_script, assert_python_ok, assert_python_failure, spawn_python, kill_python
import test_cmd_line_script

def test_dash_m_error_code_is_one():
    with CmdLineTest.setup_test_pkg() as pkg_dir:
        script_name = test_cmd_line_script._make_test_script(pkg_dir, 'other', "if __name__ == '__main__': raise ValueError")
        err = CmdLineTest.check_dash_m_failure('test_pkg.other', *test_cmd_line_script.example_args)
        CmdLineTest.assertIn(b'ValueError', err)

CmdLineTest = test_cmd_line_script.CmdLineTest()
test_dash_m_error_code_is_one()
