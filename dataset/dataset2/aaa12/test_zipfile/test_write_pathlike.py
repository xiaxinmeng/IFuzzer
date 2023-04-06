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

def test_write_pathlike():
    os.mkdir(test_zipfile.TESTFN2)
    try:
        with open(os.path.join(test_zipfile.TESTFN2, 'mod1.py'), 'w') as fp:
            fp.write('print(42)\n')
        with TemporaryFile() as t, zipfile.PyZipFile(t, 'w') as zipfp:
            zipfp.writepy(pathlib.Path(test_zipfile.TESTFN2) / 'mod1.py')
            names = zipfp.namelist()
            PyZipFileTests.assertCompiledIn('mod1.py', names)
    finally:
        rmtree(test_zipfile.TESTFN2)

PyZipFileTests = test_zipfile.PyZipFileTests()
test_write_pathlike()
