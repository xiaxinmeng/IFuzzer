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

def test_line_terminator2():
    for l in (1, 2, 3):
        TestAsynchat.line_terminator_check(b'\r\n', l)

TestAsynchat = test_asynchat.TestAsynchat()
test_line_terminator2()
