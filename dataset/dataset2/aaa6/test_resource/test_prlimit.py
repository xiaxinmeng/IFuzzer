import contextlib
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import time
import test_resource

@unittest.skipUnless(hasattr(test_resource.resource, 'prlimit'), 'no prlimit')
@support.requires_linux_version(2, 6, 36)
def test_prlimit():
    ResourceTest.assertRaises(TypeError, test_resource.resource.prlimit)
    ResourceTest.assertRaises(ProcessLookupError, test_resource.resource.prlimit, -1, test_resource.resource.RLIMIT_AS)
    limit = test_resource.resource.getrlimit(test_resource.resource.RLIMIT_AS)
    ResourceTest.assertEqual(test_resource.resource.prlimit(0, test_resource.resource.RLIMIT_AS), limit)
    ResourceTest.assertEqual(test_resource.resource.prlimit(0, test_resource.resource.RLIMIT_AS, limit), limit)

ResourceTest = test_resource.ResourceTest()
test_prlimit()
