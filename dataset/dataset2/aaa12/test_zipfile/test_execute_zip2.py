import contextlib
import importlib.util
import io
import itertools
import os
import pathlib
import posixpath
import string
import struct
import subprocess
import sys
import time
import unittest
import unittest.mock as mock
import zipfile
import functools
from tempfile import TemporaryFile
from random import randint, random, randbytes
from test.support import script_helper
from test.support import findfile, requires_zlib, requires_bz2, requires_lzma, captured_stdout
from test.support.os_helper import TESTFN, unlink, rmtree, temp_dir, temp_cwd
import email
import test
import email
import test_zipfile

@unittest.skipUnless(sys.executable, 'sys.executable required.')
@unittest.skipUnless(os.access('/bin/bash', os.X_OK), 'Test relies on #!/bin/bash working.')
def test_execute_zip2():
    output = subprocess.check_output([TestExecutablePrependedZip.exe_zip, sys.executable])
    TestExecutablePrependedZip.assertIn(b'number in executable: 5', output)

TestExecutablePrependedZip = test_zipfile.TestExecutablePrependedZip()
TestExecutablePrependedZip.setUp()
test_execute_zip2()
