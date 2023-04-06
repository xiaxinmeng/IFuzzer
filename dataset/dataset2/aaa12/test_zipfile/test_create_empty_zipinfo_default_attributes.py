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

def test_create_empty_zipinfo_default_attributes():
    """Ensure all required attributes are set."""
    zi = zipfile.ZipInfo()
    OtherTests.assertEqual(zi.orig_filename, 'NoName')
    OtherTests.assertEqual(zi.filename, 'NoName')
    OtherTests.assertEqual(zi.date_time, (1980, 1, 1, 0, 0, 0))
    OtherTests.assertEqual(zi.compress_type, zipfile.ZIP_STORED)
    OtherTests.assertEqual(zi.comment, b'')
    OtherTests.assertEqual(zi.extra, b'')
    OtherTests.assertIn(zi.create_system, (0, 3))
    OtherTests.assertEqual(zi.create_version, zipfile.DEFAULT_VERSION)
    OtherTests.assertEqual(zi.extract_version, zipfile.DEFAULT_VERSION)
    OtherTests.assertEqual(zi.reserved, 0)
    OtherTests.assertEqual(zi.flag_bits, 0)
    OtherTests.assertEqual(zi.volume, 0)
    OtherTests.assertEqual(zi.internal_attr, 0)
    OtherTests.assertEqual(zi.external_attr, 0)
    OtherTests.assertEqual(zi.file_size, 0)
    OtherTests.assertEqual(zi.compress_size, 0)

OtherTests = test_zipfile.OtherTests()
test_create_empty_zipinfo_default_attributes()
