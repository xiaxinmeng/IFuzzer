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

def test_add_file_before_1980():
    os.utime(test_zipfile.TESTFN, (0, 0))
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w') as zipfp:
        StoredTestsWithSourceFile.assertRaises(ValueError, zipfp.write, test_zipfile.TESTFN)
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', strict_timestamps=False) as zipfp:
        zipfp.write(test_zipfile.TESTFN)
        zinfo = zipfp.getinfo(test_zipfile.TESTFN)
        StoredTestsWithSourceFile.assertEqual(zinfo.date_time, (1980, 1, 1, 0, 0, 0))

StoredTestsWithSourceFile = test_zipfile.StoredTestsWithSourceFile()
test_add_file_before_1980()
