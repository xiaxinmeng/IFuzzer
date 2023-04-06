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

def test_empty_file():
    f = open(test_mmap.TESTFN, 'w+b')
    f.close()
    with open(test_mmap.TESTFN, 'rb') as f:
        MmapTests.assertRaisesRegex(ValueError, 'cannot mmap an empty file', test_mmap.mmap.mmap, f.fileno(), 0, access=test_mmap.mmap.ACCESS_READ)

MmapTests = test_mmap.MmapTests()
test_empty_file()
