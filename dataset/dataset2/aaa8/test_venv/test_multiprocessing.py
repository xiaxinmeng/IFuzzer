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

@test_venv.requireVenvCreate
def test_multiprocessing():
    """
        Test that the multiprocessing is able to spawn.
        """
    skip_if_broken_multiprocessing_synchronize()
    rmtree(BasicTest.env_dir)
    BasicTest.run_with_capture(venv.create, BasicTest.env_dir)
    envpy = os.path.join(os.path.realpath(BasicTest.env_dir), BasicTest.bindir, BasicTest.exe)
    (out, err) = test_venv.check_output([envpy, '-c', 'from multiprocessing import Pool; pool = Pool(1); print(pool.apply_async("Python".lower).get(3)); pool.terminate()'])
    BasicTest.assertEqual(out.strip(), 'python'.encode())

BasicTest = test_venv.BasicTest()
BasicTest.setUp()
test_multiprocessing()
