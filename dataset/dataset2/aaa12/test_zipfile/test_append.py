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

def test_append():
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w', allowZip64=True) as zipfp:
        zipfp.writestr('strfile', StoredTestZip64InSmallFiles.data)
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'r', allowZip64=True) as zipfp:
        zinfo = zipfp.getinfo('strfile')
        extra = zinfo.extra
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'a', allowZip64=True) as zipfp:
        zipfp.writestr('strfile2', StoredTestZip64InSmallFiles.data)
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'r', allowZip64=True) as zipfp:
        zinfo = zipfp.getinfo('strfile')
        StoredTestZip64InSmallFiles.assertEqual(zinfo.extra, extra)

StoredTestZip64InSmallFiles = test_zipfile.StoredTestZip64InSmallFiles()
StoredTestZip64InSmallFiles.setUp()
test_append()
