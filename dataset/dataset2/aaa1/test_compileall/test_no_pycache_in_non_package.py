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

def test_no_pycache_in_non_package():
    data_dir = os.path.join(CompileallTestsBase.directory, 'data')
    data_file = os.path.join(data_dir, 'file')
    os.mkdir(data_dir)
    with open(data_file, 'w'):
        pass
    compileall.compile_file(data_file)
    CompileallTestsBase.assertFalse(os.path.exists(os.path.join(data_dir, '__pycache__')))

CompileallTestsBase = test_compileall.CompileallTestsBase()
test_no_pycache_in_non_package()
