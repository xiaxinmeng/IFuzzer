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

def test_compile_workers_non_positive():
    with CompileallTestsBase.assertRaisesRegex(ValueError, 'workers must be greater or equal to 0'):
        compileall.compile_dir(CompileallTestsBase.directory, workers=-1)

CompileallTestsBase = test_compileall.CompileallTestsBase()
test_compile_workers_non_positive()
