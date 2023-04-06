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

def test_no_pip_by_default():
    rmtree(EnsurePipTest.env_dir)
    EnsurePipTest.run_with_capture(venv.create, EnsurePipTest.env_dir)
    EnsurePipTest.assert_pip_not_installed()

EnsurePipTest = test_venv.EnsurePipTest()
EnsurePipTest.setUp()
test_no_pip_by_default()
