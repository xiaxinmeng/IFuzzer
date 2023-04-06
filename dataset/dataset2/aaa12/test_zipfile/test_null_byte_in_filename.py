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

def test_null_byte_in_filename():
    """Check that a filename containing a null byte is properly
        terminated."""
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.writestr('foo.txt\x00qqq', b'O, for a Muse of Fire!')
        OtherTests.assertEqual(zipf.namelist(), ['foo.txt'])

OtherTests = test_zipfile.OtherTests()
test_null_byte_in_filename()
