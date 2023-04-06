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

def test_basic_script():
    with os_helper.temp_dir() as script_dir:
        script_name = test_cmd_line_script._make_test_script(script_dir, 'script')
        CmdLineTest._check_script(script_name, script_name, script_name, script_dir, None, importlib.machinery.SourceFileLoader, expected_cwd=script_dir)

CmdLineTest = test_cmd_line_script.CmdLineTest()
test_basic_script()
