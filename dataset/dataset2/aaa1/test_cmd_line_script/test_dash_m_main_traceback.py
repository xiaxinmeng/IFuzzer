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

def test_dash_m_main_traceback():
    with CmdLineTest.setup_test_pkg() as pkg_dir:
        main = "raise ImportError('Exception in __main__ module')"
        test_cmd_line_script._make_test_script(pkg_dir, '__main__', main)
        err = CmdLineTest.check_dash_m_failure('test_pkg')
        CmdLineTest.assertIn(b'ImportError', err)
        CmdLineTest.assertIn(b'Exception in __main__ module', err)
        CmdLineTest.assertIn(b'Traceback', err)

CmdLineTest = test_cmd_line_script.CmdLineTest()
test_dash_m_main_traceback()
