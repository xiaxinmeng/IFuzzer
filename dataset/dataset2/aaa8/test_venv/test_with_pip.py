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

@unittest.skipUnless(ctypes, 'pip requires ctypes')
@requires_zlib()
def test_with_pip():
    EnsurePipTest.do_test_with_pip(False)
    EnsurePipTest.do_test_with_pip(True)

EnsurePipTest = test_venv.EnsurePipTest()
EnsurePipTest.setUp()
test_with_pip()
