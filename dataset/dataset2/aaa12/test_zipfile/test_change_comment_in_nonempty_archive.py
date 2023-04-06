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

def test_change_comment_in_nonempty_archive():
    with zipfile.ZipFile(TESTFN, 'w', zipfile.ZIP_STORED) as zipf:
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
    with zipfile.ZipFile(TESTFN, 'a', zipfile.ZIP_STORED) as zipf:
        OtherTests.assertTrue(zipf.filelist)
        zipf.comment = b'this is a comment'
    with zipfile.ZipFile(TESTFN, 'r') as zipf:
        OtherTests.assertEqual(zipf.comment, b'this is a comment')

OtherTests = test_zipfile.OtherTests()
test_change_comment_in_nonempty_archive()
