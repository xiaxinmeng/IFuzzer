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

def test_length_0_large_offset():
    with open(TESTFN, 'wb') as f:
        f.write(115699 * b'm')
    with open(TESTFN, 'w+b') as f:
        MmapTests.assertRaises(ValueError, test_mmap.mmap.mmap, f.fileno(), 0, offset=2147418112)

MmapTests = test_mmap.MmapTests()
test_length_0_large_offset()
