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

def test_subclass():

    class anon_mmap(test_mmap.mmap.mmap):

        def __new__(klass, *args, **kwargs):
            return test_mmap.mmap.mmap.__new__(klass, -1, *args, **kwargs)
    anon_mmap(test_mmap.PAGESIZE)

MmapTests = test_mmap.MmapTests()
test_subclass()
