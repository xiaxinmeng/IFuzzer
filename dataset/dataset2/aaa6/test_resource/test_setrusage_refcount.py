import contextlib
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import time
import test_resource

@unittest.skipIf(sys.platform == 'vxworks', 'setting RLIMIT_CPU is not supported on VxWorks')
def test_setrusage_refcount():
    try:
        limits = test_resource.resource.getrlimit(test_resource.resource.RLIMIT_CPU)
    except AttributeError:
        pass
    else:

        class BadSequence:

            def __len__(ResourceTest):
                return 2

            def __getitem__(ResourceTest, key):
                if key in (0, 1):
                    return len(tuple(range(1000000)))
                raise IndexError
        test_resource.resource.setrlimit(test_resource.resource.RLIMIT_CPU, BadSequence())

ResourceTest = test_resource.ResourceTest()
test_setrusage_refcount()
