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

def test_write_while_reading():
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr('ones', TestsWithMultipleOpens.data1)
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'a', zipfile.ZIP_DEFLATED) as zipf:
        with zipf.open('ones', 'r') as r1:
            data1 = r1.read(500)
            with zipf.open('twos', 'w') as w1:
                w1.write(TestsWithMultipleOpens.data2)
            data1 += r1.read()
    TestsWithMultipleOpens.assertEqual(data1, TestsWithMultipleOpens.data1)
    with zipfile.ZipFile(test_zipfile.TESTFN2) as zipf:
        TestsWithMultipleOpens.assertEqual(zipf.read('twos'), TestsWithMultipleOpens.data2)

TestsWithMultipleOpens = test_zipfile.TestsWithMultipleOpens()
test_write_while_reading()
