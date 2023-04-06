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

@unittest.skipUnless(can_symlink(), 'Needs symlinks')
def test_symlinking():
    """
        Test symlinking works as expected
        """
    for usl in (False, True):
        builder = venv.EnvBuilder(clear=True, symlinks=usl)
        builder.create(BasicTest.env_dir)
        fn = BasicTest.get_env_file(BasicTest.bindir, BasicTest.exe)
        if usl:
            if BasicTest.cannot_link_exe:
                BasicTest.assertFalse(os.path.islink(fn))
            else:
                BasicTest.assertTrue(os.path.islink(fn))

BasicTest = test_venv.BasicTest()
BasicTest.setUp()
test_symlinking()
