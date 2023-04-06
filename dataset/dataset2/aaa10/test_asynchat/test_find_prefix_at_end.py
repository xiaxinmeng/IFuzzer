from test import support
from test.support import socket_helper
from test.support import threading_helper
import asynchat
import asyncore
import errno
import socket
import sys
import threading
import time
import unittest
import unittest.mock
import test_asynchat

def test_find_prefix_at_end():
    TestHelperFunctions.assertEqual(asynchat.find_prefix_at_end('qwerty\r', '\r\n'), 1)
    TestHelperFunctions.assertEqual(asynchat.find_prefix_at_end('qwertydkjf', '\r\n'), 0)

TestHelperFunctions = test_asynchat.TestHelperFunctions()
test_find_prefix_at_end()
