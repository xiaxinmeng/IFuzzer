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

def test_flush_return_value():
    mm = test_mmap.mmap.mmap(-1, 16)
    MmapTests.addCleanup(mm.close)
    mm.write(b'python')
    result = mm.flush()
    MmapTests.assertIsNone(result)
    if sys.platform.startswith('linux'):
        MmapTests.assertRaises(OSError, mm.flush, 1, len(b'python'))

MmapTests = test_mmap.MmapTests()
test_flush_return_value()
