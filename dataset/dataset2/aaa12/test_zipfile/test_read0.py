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

def test_read0():
    """Check that calling read(0) on a ZipExtFile object returns an empty
        string and doesn't advance file pointer."""
    with zipfile.ZipFile(TESTFN, mode='w') as zipf:
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
        with zipf.open('foo.txt') as f:
            for i in range(test_zipfile.FIXEDTEST_SIZE):
                OtherTests.assertEqual(f.read(0), b'')
            OtherTests.assertEqual(f.read(), b'O, for a Muse of Fire!')

OtherTests = test_zipfile.OtherTests()
test_read0()
