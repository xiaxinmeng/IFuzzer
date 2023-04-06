import contextlib
import sys
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import time
import test_resource

@unittest.skipUnless(sys.platform == 'linux', 'test requires Linux')
def test_linux_constants():
    for attr in ['MSGQUEUE', 'NICE', 'RTPRIO', 'RTTIME', 'SIGPENDING']:
        with contextlib.suppress(AttributeError):
            ResourceTest.assertIsInstance(getattr(test_resource.resource, 'RLIMIT_' + attr), int)

ResourceTest = test_resource.ResourceTest()
test_linux_constants()
