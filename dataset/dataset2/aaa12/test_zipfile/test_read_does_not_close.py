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

@test_zipfile.pass_alpharep
def test_read_does_not_close(TestPath, alpharep):
    alpharep = TestPath.zipfile_ondisk(alpharep)
    with zipfile.ZipFile(alpharep) as file:
        for rep in range(2):
            zipfile.Path(file, 'a.txt').read_text()

TestPath = test_zipfile.TestPath()
TestPath.setUp()
test_read_does_not_close()
