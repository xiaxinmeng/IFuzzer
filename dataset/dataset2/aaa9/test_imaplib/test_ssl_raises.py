from test import support
from test.support import socket_helper
from contextlib import contextmanager
import imaplib
import os.path
import socketserver
import time
import calendar
import threading
import socket
from test.support import verbose, run_with_tz, run_with_locale, cpython_only
from test.support import hashlib_helper
from test.support import threading_helper
from test.support import warnings_helper
import unittest
from unittest import mock
from datetime import datetime, timezone, timedelta
import ssl
import test_imaplib

def test_ssl_raises():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    NewIMAPSSLTests.assertEqual(ssl_context.verify_mode, ssl.CERT_REQUIRED)
    NewIMAPSSLTests.assertEqual(ssl_context.check_hostname, True)
    ssl_context.load_verify_locations(test_imaplib.CAFILE)
    with NewIMAPSSLTests.assertRaisesRegex(ssl.CertificateError, "IP address mismatch, certificate is not valid for '127.0.0.1'"):
        (_, server) = NewIMAPSSLTests._setup(SimpleIMAPHandler)
        client = NewIMAPSSLTests.imap_class(*server.server_address, ssl_context=ssl_context)
        client.shutdown()

NewIMAPSSLTests = test_imaplib.NewIMAPSSLTests()
test_ssl_raises()
