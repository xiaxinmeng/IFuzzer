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

def test_large_file_exception():
    for f in test_zipfile.get_files(StoredTestZip64InSmallFiles):
        StoredTestZip64InSmallFiles.large_file_exception_test(f, zipfile.ZIP_STORED)
        StoredTestZip64InSmallFiles.large_file_exception_test2(f, zipfile.ZIP_STORED)

StoredTestZip64InSmallFiles = test_zipfile.StoredTestZip64InSmallFiles()
test_large_file_exception()
