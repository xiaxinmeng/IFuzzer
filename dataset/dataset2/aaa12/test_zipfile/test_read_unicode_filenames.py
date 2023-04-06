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

@requires_zlib()
def test_read_unicode_filenames():
    fname = findfile('zip_cp437_header.zip')
    with zipfile.ZipFile(fname) as zipfp:
        for name in zipfp.namelist():
            zipfp.open(name).close()

OtherTests = test_zipfile.OtherTests()
test_read_unicode_filenames()
