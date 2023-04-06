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

def test_strip_prepend_and_ddir():
    fullpath = ['test', 'build', 'real', 'path', 'ddir']
    path = os.path.join(CompileallTestsBase.directory, *fullpath)
    os.makedirs(path)
    script_helper.make_script(path, 'test', '1 / 0')
    with CompileallTestsBase.assertRaises(ValueError):
        compileall.compile_dir(path, quiet=True, ddir='/bar', stripdir='/foo', prependdir='/bar')

CompileallTestsBase = test_compileall.CompileallTestsBase()
test_strip_prepend_and_ddir()
