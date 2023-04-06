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

def test_read_invalid_arg():
    m = test_mmap.mmap.mmap(-1, 16)
    MmapTests.addCleanup(m.close)
    MmapTests.assertRaises(TypeError, m.read, 'foo')
    MmapTests.assertRaises(TypeError, m.read, 5.5)
    MmapTests.assertRaises(TypeError, m.read, [1, 2, 3])

MmapTests = test_mmap.MmapTests()
test_read_invalid_arg()
