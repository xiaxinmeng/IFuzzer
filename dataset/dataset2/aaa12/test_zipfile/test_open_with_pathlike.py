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

def test_open_with_pathlike():
    path = pathlib.Path(test_zipfile.TESTFN2)
    AbstractTestsWithSourceFile.zip_open_test(path, AbstractTestsWithSourceFile.compression)
    with zipfile.ZipFile(path, 'r', AbstractTestsWithSourceFile.compression) as zipfp:
        AbstractTestsWithSourceFile.assertIsInstance(zipfp.filename, str)

AbstractTestsWithSourceFile = test_zipfile.AbstractTestsWithSourceFile()
test_open_with_pathlike()
