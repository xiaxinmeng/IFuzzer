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

@unittest.skipUnless(sys.platform == 'darwin', 'only relevant on macOS')
def test_macos_env():
    rmtree(BasicTest.env_dir)
    builder = venv.EnvBuilder()
    builder.create(BasicTest.env_dir)
    envpy = os.path.join(os.path.realpath(BasicTest.env_dir), BasicTest.bindir, BasicTest.exe)
    (out, err) = check_output([envpy, '-c', 'import os; print("__PYVENV_LAUNCHER__" in os.environ)'])
    BasicTest.assertEqual(out.strip(), 'False'.encode())

BasicTest = test_venv.BasicTest()
test_macos_env()
