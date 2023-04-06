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

def test_unregister_after_socket_close():
    s = BaseSelectorTestCase.SELECTOR()
    BaseSelectorTestCase.addCleanup(s.close)
    (rd, wr) = BaseSelectorTestCase.make_socketpair()
    s.register(rd, selectors.EVENT_READ)
    s.register(wr, selectors.EVENT_WRITE)
    rd.close()
    wr.close()
    s.unregister(rd)
    s.unregister(wr)

BaseSelectorTestCase = test_selectors.BaseSelectorTestCase()
test_unregister_after_socket_close()
