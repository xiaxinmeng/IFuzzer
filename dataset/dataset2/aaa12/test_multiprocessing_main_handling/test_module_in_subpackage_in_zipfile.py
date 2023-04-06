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

def test_module_in_subpackage_in_zipfile():
    with os_helper.temp_dir() as script_dir:
        (zip_name, run_name) = test_multiprocessing_main_handling._make_test_zip_pkg(script_dir, 'test_zip', 'test_pkg', 'script', depth=2)
        launch_name = test_multiprocessing_main_handling._make_launch_script(script_dir, 'launch', 'test_pkg.test_pkg.script', zip_name)
        MultiProcessingCmdLineMixin._check_script(launch_name)

MultiProcessingCmdLineMixin = test_multiprocessing_main_handling.MultiProcessingCmdLineMixin()
test_module_in_subpackage_in_zipfile()
