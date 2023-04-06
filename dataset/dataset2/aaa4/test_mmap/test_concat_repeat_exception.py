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

def test_concat_repeat_exception():
    m = test_mmap.mmap.mmap(-1, 16)
    with MmapTests.assertRaises(TypeError):
        m + m
    with MmapTests.assertRaises(TypeError):
        m * 2

MmapTests = test_mmap.MmapTests()
test_concat_repeat_exception()
