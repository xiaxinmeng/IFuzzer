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

def test_read_zip64_with_exe_prepended():
    TestExecutablePrependedZip._test_zip_works(TestExecutablePrependedZip.exe_zip64)

TestExecutablePrependedZip = test_zipfile.TestExecutablePrependedZip()
TestExecutablePrependedZip.setUp()
test_read_zip64_with_exe_prepended()
