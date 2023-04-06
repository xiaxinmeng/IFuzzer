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

def test_dash_m_bad_pyc():
    with os_helper.temp_dir() as script_dir, os_helper.change_cwd(path=script_dir):
        os.mkdir('test_pkg')
        with open('test_pkg/__init__.pyc', 'wb'):
            pass
        err = CmdLineTest.check_dash_m_failure('test_pkg')
        CmdLineTest.assertRegex(err, b'Error while finding module specification.*ImportError.*bad magic number')
        CmdLineTest.assertNotIn(b'is a package', err)
        CmdLineTest.assertNotIn(b'Traceback', err)

CmdLineTest = test_cmd_line_script.CmdLineTest()
test_dash_m_bad_pyc()
