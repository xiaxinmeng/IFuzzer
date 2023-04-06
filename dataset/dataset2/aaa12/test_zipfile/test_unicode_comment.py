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

def test_unicode_comment():
    with zipfile.ZipFile(TESTFN, 'w', zipfile.ZIP_STORED) as zipf:
        zipf.writestr('foo.txt', 'O, for a Muse of Fire!')
        with OtherTests.assertRaises(TypeError):
            zipf.comment = 'this is an error'

OtherTests = test_zipfile.OtherTests()
test_unicode_comment()
