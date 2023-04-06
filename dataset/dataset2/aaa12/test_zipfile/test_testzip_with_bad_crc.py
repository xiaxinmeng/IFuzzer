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

def test_testzip_with_bad_crc():
    """Tests that files with bad CRCs return their name from testzip."""
    zipdata = AbstractBadCrcTests.zip_with_bad_crc
    with zipfile.ZipFile(io.BytesIO(zipdata), mode='r') as zipf:
        AbstractBadCrcTests.assertEqual('afile', zipf.testzip())

AbstractBadCrcTests = test_zipfile.AbstractBadCrcTests()
test_testzip_with_bad_crc()
