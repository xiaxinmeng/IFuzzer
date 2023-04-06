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

@unittest.skipUnless(os.name == 'nt', 'requires Windows')
def test_invalid_descriptor():
    s = socket.socket()
    try:
        with MmapTests.assertRaises(OSError):
            m = mmap.mmap(s.fileno(), 10)
    finally:
        s.close()

MmapTests = test_mmap.MmapTests()
test_invalid_descriptor()
