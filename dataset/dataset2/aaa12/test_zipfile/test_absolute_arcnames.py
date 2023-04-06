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

def test_absolute_arcnames():
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', zipfile.ZIP_STORED, allowZip64=True) as zipfp:
        zipfp.write(test_zipfile.TESTFN, '/absolute')
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'r', zipfile.ZIP_STORED) as zipfp:
        StoredTestsWithSourceFile.assertEqual(zipfp.namelist(), ['absolute'])

StoredTestsWithSourceFile = test_zipfile.StoredTestsWithSourceFile()
test_absolute_arcnames()
