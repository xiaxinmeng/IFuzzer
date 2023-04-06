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

def test_close_on_exception():
    """Check that the zipfile is closed if an exception is raised in the
        'with' block."""
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w') as zipfp:
        for (fpath, fdata) in test_zipfile.SMALL_TEST_DATA:
            zipfp.writestr(fpath, fdata)
    try:
        with zipfile.ZipFile(test_zipfile.TESTFN2, 'r') as zipfp2:
            raise zipfile.BadZipFile()
    except zipfile.BadZipFile:
        OtherTests.assertIsNone(zipfp2.fp, 'zipfp is not closed')

OtherTests = test_zipfile.OtherTests()
test_close_on_exception()
