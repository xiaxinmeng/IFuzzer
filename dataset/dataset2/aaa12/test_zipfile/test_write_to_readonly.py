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

def test_write_to_readonly():
    """Check that trying to call write() on a readonly ZipFile object
        raises a ValueError."""
    with zipfile.ZipFile(test_zipfile.TESTFN2, mode='w') as zipfp:
        zipfp.writestr('somefile.txt', 'bogus')
    with zipfile.ZipFile(test_zipfile.TESTFN2, mode='r') as zipfp:
        StoredTestsWithSourceFile.assertRaises(ValueError, zipfp.write, TESTFN)
    with zipfile.ZipFile(test_zipfile.TESTFN2, mode='r') as zipfp:
        with StoredTestsWithSourceFile.assertRaises(ValueError):
            zipfp.open(TESTFN, mode='w')

StoredTestsWithSourceFile = test_zipfile.StoredTestsWithSourceFile()
test_write_to_readonly()
