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
def test_apop_normal():
    TestPOP3Class.assertOK(TestPOP3Class.client.apop('foo', 'dummypassword'))

TestPOP3Class = test_poplib.TestPOP3Class()
TestPOP3Class.setUp()
test_apop_normal()
