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

def test_devnull():
    with open(os.devnull, 'rb') as f:
        EnsurePipTest.assertEqual(f.read(), b'')
    EnsurePipTest.assertTrue(os.path.exists(os.devnull))

EnsurePipTest = test_venv.EnsurePipTest()
test_devnull()
