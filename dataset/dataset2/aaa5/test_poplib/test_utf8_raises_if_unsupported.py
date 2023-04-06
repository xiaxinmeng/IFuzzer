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

def test_utf8_raises_if_unsupported():
    TestPOP3Class.server.handler.enable_UTF8 = False
    TestPOP3Class.assertRaises(poplib.error_proto, TestPOP3Class.client.utf8)

TestPOP3Class = test_poplib.TestPOP3Class()
TestPOP3Class.setUp()
test_utf8_raises_if_unsupported()
