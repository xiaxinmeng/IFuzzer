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

def test_append_to_zip_file():
    """Test appending to an existing zipfile."""
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', zipfile.ZIP_STORED) as zipfp:
        zipfp.write(test_zipfile.TESTFN, test_zipfile.TESTFN)
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'a', zipfile.ZIP_STORED) as zipfp:
        zipfp.writestr('strfile', StoredTestsWithSourceFile.data)
        StoredTestsWithSourceFile.assertEqual(zipfp.namelist(), [test_zipfile.TESTFN, 'strfile'])

StoredTestsWithSourceFile = test_zipfile.StoredTestsWithSourceFile()
test_append_to_zip_file()
