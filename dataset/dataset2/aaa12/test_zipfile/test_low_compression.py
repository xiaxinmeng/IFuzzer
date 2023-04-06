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

def test_low_compression():
    """Check for cases where compressed data is larger than original."""
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', AbstractTestsWithSourceFile.compression) as zipfp:
        zipfp.writestr('strfile', '12')
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'r', AbstractTestsWithSourceFile.compression) as zipfp:
        with zipfp.open('strfile') as openobj:
            AbstractTestsWithSourceFile.assertEqual(openobj.read(1), b'1')
            AbstractTestsWithSourceFile.assertEqual(openobj.read(1), b'2')

AbstractTestsWithSourceFile = test_zipfile.AbstractTestsWithSourceFile()
test_low_compression()
