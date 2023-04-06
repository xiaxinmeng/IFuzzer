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

def test_many_opens():
    TestsWithMultipleOpens.make_test_archive(test_zipfile.TESTFN2)
    with zipfile.ZipFile(test_zipfile.TESTFN2, mode='r') as zipf:
        for x in range(100):
            zipf.read('ones')
            with zipf.open('ones') as zopen1:
                pass
    with open(os.devnull) as f:
        TestsWithMultipleOpens.assertLess(f.fileno(), 100)

TestsWithMultipleOpens = test_zipfile.TestsWithMultipleOpens()
TestsWithMultipleOpens.setUp()
test_many_opens()
