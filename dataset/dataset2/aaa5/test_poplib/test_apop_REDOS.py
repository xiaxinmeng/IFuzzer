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

@hashlib_helper.requires_hashdigest('md5')
def test_apop_REDOS():
    evil_welcome = b'+OK' + b'<' * 1000000
    with test_support.swap_attr(TestPOP3Class.client, 'welcome', evil_welcome):
        TestPOP3Class.assertRaises(poplib.error_proto, TestPOP3Class.client.apop, 'a', 'kb')

TestPOP3Class = test_poplib.TestPOP3Class()
TestPOP3Class.setUp()
test_apop_REDOS()
