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

def test_context():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    TestPOP3_SSLClass.assertRaises(ValueError, poplib.POP3_SSL, TestPOP3_SSLClass.server.host, TestPOP3_SSLClass.server.port, keyfile=test_poplib.CERTFILE, context=ctx)
    TestPOP3_SSLClass.assertRaises(ValueError, poplib.POP3_SSL, TestPOP3_SSLClass.server.host, TestPOP3_SSLClass.server.port, certfile=test_poplib.CERTFILE, context=ctx)
    TestPOP3_SSLClass.assertRaises(ValueError, poplib.POP3_SSL, TestPOP3_SSLClass.server.host, TestPOP3_SSLClass.server.port, keyfile=test_poplib.CERTFILE, certfile=test_poplib.CERTFILE, context=ctx)
    TestPOP3_SSLClass.client.quit()
    TestPOP3_SSLClass.client = poplib.POP3_SSL(TestPOP3_SSLClass.server.host, TestPOP3_SSLClass.server.port, context=ctx)
    TestPOP3_SSLClass.assertIsInstance(TestPOP3_SSLClass.client.sock, ssl.SSLSocket)
    TestPOP3_SSLClass.assertIs(TestPOP3_SSLClass.client.sock.context, ctx)
    TestPOP3_SSLClass.assertTrue(TestPOP3_SSLClass.client.noop().startswith(b'+OK'))

TestPOP3_SSLClass = test_poplib.TestPOP3_SSLClass()
TestPOP3_SSLClass.setUp()
test_context()
