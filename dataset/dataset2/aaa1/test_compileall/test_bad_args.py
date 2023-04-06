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

def test_bad_args():
    with HardlinkDedupTestsBase.temporary_directory():
        HardlinkDedupTestsBase.make_script('pass')
        with HardlinkDedupTestsBase.assertRaises(ValueError):
            compileall.compile_dir(HardlinkDedupTestsBase.path, quiet=True, optimize=0, hardlink_dupes=True)
        with HardlinkDedupTestsBase.assertRaises(ValueError):
            compileall.compile_dir(HardlinkDedupTestsBase.path, quiet=True, optimize=[0, 0], hardlink_dupes=True)

HardlinkDedupTestsBase = test_compileall.HardlinkDedupTestsBase()
HardlinkDedupTestsBase.setUp()
test_bad_args()
