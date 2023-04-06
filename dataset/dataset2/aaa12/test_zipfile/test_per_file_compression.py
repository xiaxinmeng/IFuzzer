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

def test_per_file_compression():
    """Check that files within a Zip archive can have different
        compression options."""
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w') as zipfp:
        zipfp.write(TESTFN, 'storeme', zipfile.ZIP_STORED)
        zipfp.write(TESTFN, 'deflateme', zipfile.ZIP_DEFLATED)
        sinfo = zipfp.getinfo('storeme')
        dinfo = zipfp.getinfo('deflateme')
        DeflateTestsWithSourceFile.assertEqual(sinfo.compress_type, zipfile.ZIP_STORED)
        DeflateTestsWithSourceFile.assertEqual(dinfo.compress_type, zipfile.ZIP_DEFLATED)

DeflateTestsWithSourceFile = test_zipfile.DeflateTestsWithSourceFile()
test_per_file_compression()
