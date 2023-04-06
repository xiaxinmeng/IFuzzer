import ensurepip
import os
import os.path
import re
import shutil
import struct
import subprocess
import sys
import tempfile
from test.support import captured_stdout, captured_stderr, requires_zlib, skip_if_broken_multiprocessing_synchronize
from test.support.os_helper import can_symlink, EnvironmentVarGuard, rmtree
import unittest
import venv
from unittest.mock import patch
import ctypes
import test_venv

def test_unoverwritable_fails():
    for paths in BasicTest.ENV_SUBDIRS[:3]:
        fn = os.path.join(BasicTest.env_dir, *paths)
        with open(fn, 'wb') as f:
            f.write(b'')
        BasicTest.assertRaises((ValueError, OSError), venv.create, BasicTest.env_dir)
        BasicTest.clear_directory(BasicTest.env_dir)

BasicTest = test_venv.BasicTest()
BasicTest.setUp()
test_unoverwritable_fails()
