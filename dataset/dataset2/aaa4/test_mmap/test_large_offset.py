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

def test_large_offset():
    with LargeMmapTests._make_test_file(5637144575, b' ') as f:
        with test_mmap.mmap.mmap(f.fileno(), 0, offset=5368709120, access=test_mmap.mmap.ACCESS_READ) as m:
            LargeMmapTests.assertEqual(m[268435455], 32)

LargeMmapTests = test_mmap.LargeMmapTests()
test_large_offset()
