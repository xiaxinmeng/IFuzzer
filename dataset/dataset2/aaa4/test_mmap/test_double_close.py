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

def test_double_close():
    with open(test_mmap.TESTFN, 'wb+') as f:
        f.write(2 ** 16 * b'a')
    with open(test_mmap.TESTFN, 'rb') as f:
        mf = test_mmap.mmap.mmap(f.fileno(), 2 ** 16, access=test_mmap.mmap.ACCESS_READ)
        mf.close()
        mf.close()

MmapTests = test_mmap.MmapTests()
test_double_close()
