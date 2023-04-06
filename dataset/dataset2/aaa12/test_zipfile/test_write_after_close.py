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

def test_write_after_close():
    data = b'content'
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', AbstractWriterTests.compression) as zipf:
        w = zipf.open('test', 'w')
        w.write(data)
        w.close()
        AbstractWriterTests.assertTrue(w.closed)
        AbstractWriterTests.assertRaises(ValueError, w.write, b'')
        AbstractWriterTests.assertEqual(zipf.read('test'), data)

AbstractWriterTests = test_zipfile.AbstractWriterTests()
test_write_after_close()