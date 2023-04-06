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

def test_ddir_empty_only_one_worker():
    """Recursive compile_dir ddir='' contains package paths; bpo39769."""
    return CompileallTestsBase._test_ddir_only(ddir='', parallel=False)

CompileallTestsBase = test_compileall.CompileallTestsBase()
test_ddir_empty_only_one_worker()
