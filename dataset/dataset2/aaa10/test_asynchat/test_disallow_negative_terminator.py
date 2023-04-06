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

def test_disallow_negative_terminator():
    client = asynchat.async_chat()
    TestNotConnected.assertRaises(ValueError, client.set_terminator, -1)

TestNotConnected = test_asynchat.TestNotConnected()
test_disallow_negative_terminator()
