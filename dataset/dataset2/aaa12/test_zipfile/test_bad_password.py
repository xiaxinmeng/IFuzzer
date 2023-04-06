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

def test_bad_password():
    DecryptionTests.zip.setpassword(b'perl')
    DecryptionTests.assertRaises(RuntimeError, DecryptionTests.zip.read, 'test.txt')
    DecryptionTests.zip2.setpassword(b'perl')
    DecryptionTests.assertRaises(RuntimeError, DecryptionTests.zip2.read, 'zero')

DecryptionTests = test_zipfile.DecryptionTests()
DecryptionTests.setUp()
test_bad_password()
