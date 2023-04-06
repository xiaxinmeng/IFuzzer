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

def test_duplicated_levels():
    with HardlinkDedupTestsBase.temporary_directory():
        script = HardlinkDedupTestsBase.make_script(HardlinkDedupTestsBase.create_code())
        HardlinkDedupTestsBase.compile_dir(optimize=[1, 0, 1, 0])
        pyc1 = get_pyc(script, 0)
        pyc2 = get_pyc(script, 1)
        HardlinkDedupTestsBase.assertTrue(is_hardlink(pyc1, pyc2))

HardlinkDedupTestsBase = test_compileall.HardlinkDedupTestsBase()
test_duplicated_levels()
