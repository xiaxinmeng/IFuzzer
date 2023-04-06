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

@unittest.skipIf(os.name == 'nt', 'cannot resize anonymous mmaps on Windows')
def test_resize_past_pos():
    m = test_mmap.mmap.mmap(-1, 8192)
    MmapTests.addCleanup(m.close)
    m.read(5000)
    try:
        m.resize(4096)
    except SystemError:
        MmapTests.skipTest('resizing not supported')
    MmapTests.assertEqual(m.read(14), b'')
    MmapTests.assertRaises(ValueError, m.read_byte)
    MmapTests.assertRaises(ValueError, m.write_byte, 42)
    MmapTests.assertRaises(ValueError, m.write, b'abc')

MmapTests = test_mmap.MmapTests()
test_resize_past_pos()
