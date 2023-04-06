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

def test_zipfile_with_short_extra_field():
    """If an extra field in the header is less than 4 bytes, skip it."""
    zipdata = b'PK\x03\x04\x14\x00\x00\x00\x00\x00\x93\x9b\xad@\x8b\x9e\xd9\xd3\x01\x00\x00\x00\x01\x00\x00\x00\x03\x00\x03\x00abc\x00\x00\x00APK\x01\x02\x14\x03\x14\x00\x00\x00\x00\x00\x93\x9b\xad@\x8b\x9e\xd9\xd3\x01\x00\x00\x00\x01\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81\x00\x00\x00\x00abc\x00\x00PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x003\x00\x00\x00%\x00\x00\x00\x00\x00'
    with zipfile.ZipFile(io.BytesIO(zipdata), 'r') as zipf:
        OtherTests.assertIsNone(zipf.testzip())

OtherTests = test_zipfile.OtherTests()
test_zipfile_with_short_extra_field()
