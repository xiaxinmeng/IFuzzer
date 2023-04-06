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

def test_context_manager_exception():
    with MmapTests.assertRaises(Exception) as exc:
        with test_mmap.mmap.mmap(-1, 10) as m:
            raise OSError
    MmapTests.assertIsInstance(exc.exception, OSError, 'wrong exception raised in context manager')
    MmapTests.assertTrue(m.closed, 'context manager failed')

MmapTests = test_mmap.MmapTests()
test_context_manager_exception()
