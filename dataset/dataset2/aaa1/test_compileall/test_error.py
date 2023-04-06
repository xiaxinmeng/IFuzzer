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

def test_error():
    try:
        orig_stdout = sys.stdout
        sys.stdout = io.TextIOWrapper(io.BytesIO(), encoding='ascii')
        compileall.compile_dir(EncodingTest.directory)
    finally:
        sys.stdout = orig_stdout

EncodingTest = test_compileall.EncodingTest()
test_error()
