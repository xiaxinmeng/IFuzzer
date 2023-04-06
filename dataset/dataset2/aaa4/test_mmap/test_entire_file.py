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

def test_entire_file():
    with open(test_mmap.TESTFN, 'wb+') as f:
        f.write(2 ** 16 * b'm')
    with open(test_mmap.TESTFN, 'rb+') as f, test_mmap.mmap.mmap(f.fileno(), 0) as mf:
        MmapTests.assertEqual(len(mf), 2 ** 16, 'Map size should equal file size.')
        MmapTests.assertEqual(mf.read(2 ** 16), 2 ** 16 * b'm')

MmapTests = test_mmap.MmapTests()
test_entire_file()
