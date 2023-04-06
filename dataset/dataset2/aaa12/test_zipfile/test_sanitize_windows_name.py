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

def test_sanitize_windows_name():
    san = zipfile.ZipFile._sanitize_windows_name
    ExtractTests.assertEqual(san(',,?,C:,foo,bar/z', ','), '_,C_,foo,bar/z')
    ExtractTests.assertEqual(san('a\\b,c<d>e|f"g?h*i', ','), 'a\\b,c_d_e_f_g_h_i')
    ExtractTests.assertEqual(san('../../foo../../ba..r', '/'), 'foo/ba..r')

ExtractTests = test_zipfile.ExtractTests()
test_sanitize_windows_name()
