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

def test_per_file_compresslevel():
    """Check that files within a Zip archive can have different
        compression levels."""
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', compresslevel=1) as zipfp:
        zipfp.write(TESTFN, 'compress_1')
        zipfp.write(TESTFN, 'compress_9', compresslevel=9)
        one_info = zipfp.getinfo('compress_1')
        nine_info = zipfp.getinfo('compress_9')
        AbstractTestsWithSourceFile.assertEqual(one_info._compresslevel, 1)
        AbstractTestsWithSourceFile.assertEqual(nine_info._compresslevel, 9)

AbstractTestsWithSourceFile = test_zipfile.AbstractTestsWithSourceFile()
test_per_file_compresslevel()
