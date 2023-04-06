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

def test_write_returning_the_number_of_bytes_written():
    mm = test_mmap.mmap.mmap(-1, 16)
    MmapTests.assertEqual(mm.write(b''), 0)
    MmapTests.assertEqual(mm.write(b'x'), 1)
    MmapTests.assertEqual(mm.write(b'yz'), 2)
    MmapTests.assertEqual(mm.write(b'python'), 6)

MmapTests = test_mmap.MmapTests()
test_write_returning_the_number_of_bytes_written()
