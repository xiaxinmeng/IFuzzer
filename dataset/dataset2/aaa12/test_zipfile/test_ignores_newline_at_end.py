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

def test_ignores_newline_at_end():
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', zipfile.ZIP_STORED) as zipfp:
        zipfp.write(TESTFN, TESTFN)
    with open(test_zipfile.TESTFN2, 'a') as f:
        f.write('\r\n\x00\x00\x00')
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'r') as zipfp:
        StoredTestsWithSourceFile.assertIsInstance(zipfp, zipfile.ZipFile)

StoredTestsWithSourceFile = test_zipfile.StoredTestsWithSourceFile()
test_ignores_newline_at_end()
