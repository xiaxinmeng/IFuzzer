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

def test_open_write():
    """
        If the zipfile is open for write, it should be possible to
        write bytes or text to it.
        """
    zf = zipfile.Path(zipfile.ZipFile(io.BytesIO(), mode='w'))
    with zf.joinpath('file.bin').open('wb') as strm:
        strm.write(b'binary contents')
    with zf.joinpath('file.txt').open('w') as strm:
        strm.write('text file')

UnseekableTests = test_zipfile.UnseekableTests()
test_open_write()
