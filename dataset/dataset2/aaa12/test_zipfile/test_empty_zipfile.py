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

def test_empty_zipfile():
    zipf = zipfile.ZipFile(TESTFN, mode='w')
    zipf.close()
    try:
        zipf = zipfile.ZipFile(TESTFN, mode='r')
    except zipfile.BadZipFile:
        OtherTests.fail("Unable to create empty ZIP file in 'w' mode")
    zipf = zipfile.ZipFile(TESTFN, mode='a')
    zipf.close()
    try:
        zipf = zipfile.ZipFile(TESTFN, mode='r')
    except:
        OtherTests.fail("Unable to create empty ZIP file in 'a' mode")

OtherTests = test_zipfile.OtherTests()
test_empty_zipfile()
