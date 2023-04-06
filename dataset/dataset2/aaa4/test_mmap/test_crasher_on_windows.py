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
def test_crasher_on_windows():
    m = mmap.mmap(-1, 1000, tagname='foo')
    try:
        mmap.mmap(-1, 5000, tagname='foo')[:]
    except:
        pass
    m.close()
    with open(TESTFN, 'wb') as fp:
        fp.write(b'x' * 10)
    f = open(TESTFN, 'r+b')
    m = mmap.mmap(f.fileno(), 0)
    f.close()
    try:
        m.resize(0)
    except:
        pass
    try:
        m[:]
    except:
        pass
    m.close()

MmapTests = test_mmap.MmapTests()
test_crasher_on_windows()
