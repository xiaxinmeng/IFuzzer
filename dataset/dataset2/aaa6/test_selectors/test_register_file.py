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

def test_register_file():
    s = EpollSelectorTestCase.SELECTOR()
    with tempfile.NamedTemporaryFile() as f:
        with EpollSelectorTestCase.assertRaises(IOError):
            s.register(f, selectors.EVENT_READ)
        with EpollSelectorTestCase.assertRaises(KeyError):
            s.get_key(f)

EpollSelectorTestCase = test_selectors.EpollSelectorTestCase()
test_register_file()
