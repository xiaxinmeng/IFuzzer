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

def test_unsupported_compression():
    data = b'PK\x03\x04.\x00\x00\x00\x01\x00\xe4C\xa1@\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00x\x03\x00PK\x01\x02.\x03.\x00\x00\x00\x01\x00\xe4C\xa1@\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x01\x00\x00\x00\x00xPK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00/\x00\x00\x00!\x00\x00\x00\x00\x00'
    with zipfile.ZipFile(io.BytesIO(data), 'r') as zipf:
        OtherTests.assertRaises(NotImplementedError, zipf.open, 'x')

OtherTests = test_zipfile.OtherTests()
test_unsupported_compression()
