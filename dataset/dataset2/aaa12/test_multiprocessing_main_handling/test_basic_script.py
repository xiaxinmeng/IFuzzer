from test import support
from test.support import import_helper
import importlib
import importlib.machinery
import unittest
import sys
import os
import os.path
import py_compile
from test.support import os_helper
from test.support.script_helper import make_pkg, make_script, make_zip_pkg, make_zip_script, assert_python_ok
import multiprocessing
import test_multiprocessing_main_handling

def test_basic_script():
    with os_helper.temp_dir() as script_dir:
        script_name = test_multiprocessing_main_handling._make_test_script(script_dir, 'script')
        MultiProcessingCmdLineMixin._check_script(script_name)

MultiProcessingCmdLineMixin = test_multiprocessing_main_handling.MultiProcessingCmdLineMixin()
MultiProcessingCmdLineMixin.setUp()
test_basic_script()
