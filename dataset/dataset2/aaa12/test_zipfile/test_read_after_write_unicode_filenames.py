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

def test_read_after_write_unicode_filenames():
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w') as zipfp:
        zipfp.writestr('приклад', b'sample')
        OtherTests.assertEqual(zipfp.read('приклад'), b'sample')

OtherTests = test_zipfile.OtherTests()
test_read_after_write_unicode_filenames()
