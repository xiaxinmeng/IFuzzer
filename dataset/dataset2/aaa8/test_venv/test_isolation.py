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

def test_isolation():
    """
        Test isolation from system site-packages
        """
    for (ssp, s) in ((True, 'true'), (False, 'false')):
        builder = venv.EnvBuilder(clear=True, system_site_packages=ssp)
        builder.create(BasicTest.env_dir)
        data = BasicTest.get_text_file_contents('pyvenv.cfg')
        BasicTest.assertIn('include-system-site-packages = %s\n' % s, data)

BasicTest = test_venv.BasicTest()
BasicTest.setUp()
test_isolation()
