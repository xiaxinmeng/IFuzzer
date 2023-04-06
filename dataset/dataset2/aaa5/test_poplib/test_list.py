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

def test_list():
    TestPOP3Class.assertEqual(TestPOP3Class.client.list()[1:], ([b'1 1', b'2 2', b'3 3', b'4 4', b'5 5'], 25))
    TestPOP3Class.assertTrue(TestPOP3Class.client.list('1').endswith(b'OK 1 1'))

TestPOP3Class = test_poplib.TestPOP3Class()
TestPOP3Class.setUp()
test_list()
