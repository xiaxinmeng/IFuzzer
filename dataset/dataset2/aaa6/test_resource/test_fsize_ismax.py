import contextlib
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import time
import test_resource

@unittest.skipIf(sys.platform == 'vxworks', 'setting RLIMIT_FSIZE is not supported on VxWorks')
def test_fsize_ismax():
    try:
        (cur, max) = test_resource.resource.getrlimit(test_resource.resource.RLIMIT_FSIZE)
    except AttributeError:
        pass
    else:
        ResourceTest.assertEqual(test_resource.resource.RLIM_INFINITY, max)
        test_resource.resource.setrlimit(test_resource.resource.RLIMIT_FSIZE, (cur, max))

ResourceTest = test_resource.ResourceTest()
test_fsize_ismax()
