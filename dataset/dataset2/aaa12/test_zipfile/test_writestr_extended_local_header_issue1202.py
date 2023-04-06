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

def test_writestr_extended_local_header_issue1202():
    with zipfile.ZipFile(test_zipfile.TESTFN2, 'w') as orig_zip:
        for data in 'abcdefghijklmnop':
            zinfo = zipfile.ZipInfo(data)
            zinfo.flag_bits |= 8
            orig_zip.writestr(zinfo, data)

OtherTests = test_zipfile.OtherTests()
test_writestr_extended_local_header_issue1202()
