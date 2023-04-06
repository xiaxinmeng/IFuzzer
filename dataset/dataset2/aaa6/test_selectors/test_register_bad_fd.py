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

def test_register_bad_fd():
    s = KqueueSelectorTestCase.SELECTOR()
    bad_f = os_helper.make_bad_fd()
    with KqueueSelectorTestCase.assertRaises(OSError) as cm:
        s.register(bad_f, selectors.EVENT_READ)
    KqueueSelectorTestCase.assertEqual(cm.exception.errno, errno.EBADF)
    with KqueueSelectorTestCase.assertRaises(KeyError):
        s.get_key(bad_f)

KqueueSelectorTestCase = test_selectors.KqueueSelectorTestCase()
test_register_bad_fd()
