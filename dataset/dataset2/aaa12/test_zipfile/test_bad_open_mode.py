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

def test_bad_open_mode():
    """Check that bad modes passed to ZipFile.open are caught."""
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    with zipfile.ZipFile(TESTFN, mode='r') as zipf:
        zipf.read('foo.txt')
        OtherTests.assertRaises(ValueError, zipf.open, 'foo.txt', 'q')
        OtherTests.assertRaises(ValueError, zipf.open, 'foo.txt', 'U')
        OtherTests.assertRaises(ValueError, zipf.open, 'foo.txt', 'rU')

OtherTests = test_zipfile.OtherTests()
test_bad_open_mode()
