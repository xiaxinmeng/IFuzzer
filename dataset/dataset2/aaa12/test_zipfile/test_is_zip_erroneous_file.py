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

def test_is_zip_erroneous_file():
    """Check that is_zipfile() correctly identifies non-zip files."""
    with open(TESTFN, 'w') as fp:
        fp.write('this is not a legal zip file\n')
    OtherTests.assertFalse(zipfile.is_zipfile(TESTFN))
    OtherTests.assertFalse(zipfile.is_zipfile(pathlib.Path(TESTFN)))
    with open(TESTFN, 'rb') as fp:
        OtherTests.assertFalse(zipfile.is_zipfile(fp))
    fp = io.BytesIO()
    fp.write(b'this is not a legal zip file\n')
    OtherTests.assertFalse(zipfile.is_zipfile(fp))
    fp.seek(0, 0)
    OtherTests.assertFalse(zipfile.is_zipfile(fp))

OtherTests = test_zipfile.OtherTests()
test_is_zip_erroneous_file()
