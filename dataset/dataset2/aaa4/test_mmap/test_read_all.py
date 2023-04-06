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

def test_read_all():
    m = test_mmap.mmap.mmap(-1, 16)
    MmapTests.addCleanup(m.close)
    m.write(bytes(range(16)))
    m.seek(0)
    MmapTests.assertEqual(m.read(), bytes(range(16)))
    m.seek(8)
    MmapTests.assertEqual(m.read(), bytes(range(8, 16)))
    m.seek(16)
    MmapTests.assertEqual(m.read(), b'')
    m.seek(3)
    MmapTests.assertEqual(m.read(None), bytes(range(3, 16)))
    m.seek(4)
    MmapTests.assertEqual(m.read(-1), bytes(range(4, 16)))
    m.seek(5)
    MmapTests.assertEqual(m.read(-2), bytes(range(5, 16)))
    m.seek(9)
    MmapTests.assertEqual(m.read(-42), bytes(range(9, 16)))

MmapTests = test_mmap.MmapTests()
test_read_all()
