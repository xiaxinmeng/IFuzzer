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

def test_bad_file_desc():
    MmapTests.assertRaises(OSError, test_mmap.mmap.mmap, -2, 4096)

MmapTests = test_mmap.MmapTests()
test_bad_file_desc()
