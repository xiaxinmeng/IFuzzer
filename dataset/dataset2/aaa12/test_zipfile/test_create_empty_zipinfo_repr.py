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

def test_create_empty_zipinfo_repr():
    """Before bpo-26185, repr() on empty ZipInfo object was failing."""
    zi = zipfile.ZipInfo(filename='empty')
    OtherTests.assertEqual(repr(zi), "<ZipInfo filename='empty' file_size=0>")

OtherTests = test_zipfile.OtherTests()
test_create_empty_zipinfo_repr()
