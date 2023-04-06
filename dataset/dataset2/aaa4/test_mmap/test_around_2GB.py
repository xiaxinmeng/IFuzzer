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

@unittest.skipUnless(sys.maxsize > _4G, 'test cannot run on 32-bit systems')
def test_around_2GB():
    LargeMmapTests._test_around_boundary(_2G)

LargeMmapTests = test_mmap.LargeMmapTests()
test_around_2GB()
