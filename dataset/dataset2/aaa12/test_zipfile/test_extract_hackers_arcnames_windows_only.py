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

@unittest.skipIf(os.path.sep != '\\', 'Requires \\ as path separator.')
def test_extract_hackers_arcnames_windows_only():
    """Test combination of path fixing and windows name sanitization."""
    windows_hacknames = [('..\\foo\\bar', 'foo/bar'), ('..\\/foo\\/bar', 'foo/bar'), ('foo/\\..\\/bar', 'foo/bar'), ('foo\\/../\\bar', 'foo/bar'), ('C:foo/bar', 'foo/bar'), ('C:/foo/bar', 'foo/bar'), ('C://foo/bar', 'foo/bar'), ('C:\\foo\\bar', 'foo/bar'), ('//conky/mountpoint/foo/bar', 'foo/bar'), ('\\\\conky\\mountpoint\\foo\\bar', 'foo/bar'), ('///conky/mountpoint/foo/bar', 'conky/mountpoint/foo/bar'), ('\\\\\\conky\\mountpoint\\foo\\bar', 'conky/mountpoint/foo/bar'), ('//conky//mountpoint/foo/bar', 'conky/mountpoint/foo/bar'), ('\\\\conky\\\\mountpoint\\foo\\bar', 'conky/mountpoint/foo/bar'), ('//?/C:/foo/bar', 'foo/bar'), ('\\\\?\\C:\\foo\\bar', 'foo/bar'), ('C:/../C:/foo/bar', 'C_/foo/bar'), ('a:b\\c<d>e|f"g?h*i', 'b/c_d_e_f_g_h_i'), ('../../foo../../ba..r', 'foo/ba..r')]
    ExtractTests._test_extract_hackers_arcnames(windows_hacknames)

ExtractTests = test_zipfile.ExtractTests()
test_extract_hackers_arcnames_windows_only()
