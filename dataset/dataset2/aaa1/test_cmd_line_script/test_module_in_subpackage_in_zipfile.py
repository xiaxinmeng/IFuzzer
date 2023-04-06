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

def test_module_in_subpackage_in_zipfile():
    with os_helper.temp_dir() as script_dir:
        (zip_name, run_name) = test_cmd_line_script._make_test_zip_pkg(script_dir, 'test_zip', 'test_pkg', 'script', depth=2)
        CmdLineTest._check_script(['-m', 'test_pkg.test_pkg.script'], run_name, run_name, script_dir, 'test_pkg.test_pkg', zipimport.zipimporter, PYTHONPATH=zip_name, cwd=script_dir)

CmdLineTest = test_cmd_line_script.CmdLineTest()
test_module_in_subpackage_in_zipfile()
