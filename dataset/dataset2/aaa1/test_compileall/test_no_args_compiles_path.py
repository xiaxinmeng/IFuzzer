import compileall
import contextlib
import filecmp
import importlib.util
import io
import itertools
import os
import pathlib
import py_compile
import shutil
import struct
import sys
import tempfile
import test.test_importlib.util
import time
import unittest
from unittest import mock, skipUnless
from concurrent.futures import ProcessPoolExecutor
from test import support
from test.support import os_helper
from test.support import script_helper

import test_compileall

def test_no_args_compiles_path():
    CommandLineTestsBase._skip_if_sys_path_not_writable()
    bazfn = script_helper.make_script(CommandLineTestsBase.directory, 'baz', '')
    CommandLineTestsBase.assertRunOK(PYTHONPATH=CommandLineTestsBase.directory)
    CommandLineTestsBase.assertCompiled(bazfn)
    CommandLineTestsBase.assertNotCompiled(CommandLineTestsBase.initfn)
    CommandLineTestsBase.assertNotCompiled(CommandLineTestsBase.barfn)

CommandLineTestsBase = test_compileall.CommandLineTestsBase()
test_no_args_compiles_path()
