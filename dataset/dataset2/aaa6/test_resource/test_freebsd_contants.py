import contextlib
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import time
import test_resource

def test_freebsd_contants():
    for attr in ['SWAP', 'SBSIZE', 'NPTS']:
        with contextlib.suppress(AttributeError):
            ResourceTest.assertIsInstance(getattr(test_resource.resource, 'RLIMIT_' + attr), int)

ResourceTest = test_resource.ResourceTest()
test_freebsd_contants()
