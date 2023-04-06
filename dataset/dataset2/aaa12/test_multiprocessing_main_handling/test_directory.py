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

def test_directory():
    source = MultiProcessingCmdLineMixin.main_in_children_source
    with os_helper.temp_dir() as script_dir:
        script_name = test_multiprocessing_main_handling._make_test_script(script_dir, '__main__', source=source)
        MultiProcessingCmdLineMixin._check_script(script_dir)

MultiProcessingCmdLineMixin = test_multiprocessing_main_handling.MultiProcessingCmdLineMixin()
test_directory()
