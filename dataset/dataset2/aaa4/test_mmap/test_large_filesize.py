from test.support import requires, _2G, _4G, gc_collect, cpython_only
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink
import unittest
import os
import re
import itertools
import socket
import sys
import weakref
import test_mmap

def test_large_filesize():
    with LargeMmapTests._make_test_file(6442450943, b' ') as f:
        if sys.maxsize < 6442450944:
            with LargeMmapTests.assertRaises(OverflowError):
                test_mmap.mmap.mmap(f.fileno(), 6442450944, access=test_mmap.mmap.ACCESS_READ)
            with LargeMmapTests.assertRaises(ValueError):
                test_mmap.mmap.mmap(f.fileno(), 0, access=test_mmap.mmap.ACCESS_READ)
        with test_mmap.mmap.mmap(f.fileno(), 65536, access=test_mmap.mmap.ACCESS_READ) as m:
            LargeMmapTests.assertEqual(m.size(), 6442450944)

LargeMmapTests = test_mmap.LargeMmapTests()
test_large_filesize()
