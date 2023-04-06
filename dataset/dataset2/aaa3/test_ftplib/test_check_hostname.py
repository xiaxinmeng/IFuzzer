import ftplib
import asyncore
import asynchat
import socket
import io
import errno
import os
import threading
import time
import ssl
from unittest import TestCase, skipUnless
from test import support
from test.support import threading_helper
from test.support import socket_helper
from test.support import warnings_helper
from test.support.socket_helper import HOST, HOSTv6
import test_ftplib

@skipUnless(False, 'FIXME: bpo-32706')
def test_check_hostname():
    TestTLS_FTPClass.client.quit()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    TestTLS_FTPClass.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    TestTLS_FTPClass.assertEqual(ctx.check_hostname, True)
    ctx.load_verify_locations(CAFILE)
    TestTLS_FTPClass.client = ftplib.FTP_TLS(context=ctx, timeout=TIMEOUT)
    TestTLS_FTPClass.client.connect(TestTLS_FTPClass.server.host, TestTLS_FTPClass.server.port)
    with TestTLS_FTPClass.assertRaises(ssl.CertificateError):
        TestTLS_FTPClass.client.auth()
    TestTLS_FTPClass.client.connect(TestTLS_FTPClass.server.host, TestTLS_FTPClass.server.port)
    TestTLS_FTPClass.client.prot_p()
    with TestTLS_FTPClass.assertRaises(ssl.CertificateError):
        with TestTLS_FTPClass.client.transfercmd('list') as sock:
            pass
    TestTLS_FTPClass.client.quit()
    TestTLS_FTPClass.client.connect('localhost', TestTLS_FTPClass.server.port)
    TestTLS_FTPClass.client.auth()
    TestTLS_FTPClass.client.quit()
    TestTLS_FTPClass.client.connect('localhost', TestTLS_FTPClass.server.port)
    TestTLS_FTPClass.client.prot_p()
    with TestTLS_FTPClass.client.transfercmd('list') as sock:
        pass

TestTLS_FTPClass = test_ftplib.TestTLS_FTPClass()
test_check_hostname()
