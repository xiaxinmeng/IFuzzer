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

def test_non_ascii_byte():
    for b in (129, 200, 255):
        m = test_mmap.mmap.mmap(-1, 1)
        m.write_byte(b)
        MmapTests.assertEqual(m[0], b)
        m.seek(0)
        MmapTests.assertEqual(m.read_byte(), b)
        m.close()

MmapTests = test_mmap.MmapTests()
test_non_ascii_byte()
