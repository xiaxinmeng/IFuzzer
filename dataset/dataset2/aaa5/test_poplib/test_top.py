import poplib
import asyncore
import asynchat
import socket
import os
import errno
import threading
from unittest import TestCase, skipUnless
from test import support as test_support
from test.support import hashlib_helper
from test.support import socket_helper
from test.support import threading_helper
import ssl
from test.test_ftplib import SSLConnection
import test_poplib

def test_top():
    expected = (b'+OK 116 bytes', [b'From: postmaster@python.org', b'Content-Type: text/plain', b'MIME-Version: 1.0', b'Subject: Dummy', b'', b'line1', b'line2', b'line3'], 113)
    TestPOP3Class.assertEqual(TestPOP3Class.client.top(1, 1), expected)

TestPOP3Class = test_poplib.TestPOP3Class()
TestPOP3Class.setUp()
test_top()
