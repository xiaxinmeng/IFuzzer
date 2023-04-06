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

def test_empty_select_timeout():
    s = KqueueSelectorTestCase.SELECTOR()
    KqueueSelectorTestCase.addCleanup(s.close)
    t0 = time()
    KqueueSelectorTestCase.assertEqual(s.select(1), [])
    t1 = time()
    dt = t1 - t0
    KqueueSelectorTestCase.assertTrue(0.8 <= dt <= 2.0, dt)

KqueueSelectorTestCase = test_selectors.KqueueSelectorTestCase()
test_empty_select_timeout()
