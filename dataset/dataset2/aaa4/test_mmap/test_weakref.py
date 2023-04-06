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

def test_weakref():
    mm = test_mmap.mmap.mmap(-1, 16)
    wr = weakref.ref(mm)
    MmapTests.assertIs(wr(), mm)
    del mm
    gc_collect()
    MmapTests.assertIs(wr(), None)

MmapTests = test_mmap.MmapTests()
test_weakref()
