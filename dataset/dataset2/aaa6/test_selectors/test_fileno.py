import errno
import os
import random
import selectors
import signal
import socket
import sys
from test import support
from test.support import os_helper
from test.support import socket_helper
from time import sleep
import unittest
import unittest.mock
import tempfile
from time import monotonic as time
import resource
import test_selectors

def test_fileno():
    s = BaseSelectorTestCase.SELECTOR()
    BaseSelectorTestCase.addCleanup(s.close)
    if hasattr(s, 'fileno'):
        fd = s.fileno()
        BaseSelectorTestCase.assertTrue(isinstance(fd, int))
        BaseSelectorTestCase.assertGreaterEqual(fd, 0)

BaseSelectorTestCase = test_selectors.BaseSelectorTestCase()
test_fileno()
