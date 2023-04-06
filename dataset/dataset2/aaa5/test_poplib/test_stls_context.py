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

@test_poplib.requires_ssl
def test_stls_context():
    expected = b'+OK Begin TLS negotiation'
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_verify_locations(test_poplib.CAFILE)
    TestPOP3Class.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    TestPOP3Class.assertEqual(ctx.check_hostname, True)
    with TestPOP3Class.assertRaises(ssl.CertificateError):
        resp = TestPOP3Class.client.stls(context=ctx)
    TestPOP3Class.client = poplib.POP3('localhost', TestPOP3Class.server.port, timeout=test_support.LOOPBACK_TIMEOUT)
    resp = TestPOP3Class.client.stls(context=ctx)
    TestPOP3Class.assertEqual(resp, expected)

TestPOP3Class = test_poplib.TestPOP3Class()
TestPOP3Class.setUp()
test_stls_context()
