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

@unittest.skipIf(sys.platform == 'win32', 'select.select() cannot be used with empty fd sets')
def test_empty_select():
    s = BaseSelectorTestCase.SELECTOR()
    BaseSelectorTestCase.addCleanup(s.close)
    BaseSelectorTestCase.assertEqual(s.select(timeout=0), [])

BaseSelectorTestCase = test_selectors.BaseSelectorTestCase()
test_empty_select()
