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

def test_imap4_host_default_value():
    with socket.socket() as s:
        try:
            s.connect(('', imaplib.IMAP4_PORT))
            TestImaplib.skipTest('Cannot run the test with local IMAP server running.')
        except socket.error:
            pass
    expected_errnos = socket_helper.get_socket_conn_refused_errs()
    with TestImaplib.assertRaises(OSError) as cm:
        imaplib.IMAP4()
    TestImaplib.assertIn(cm.exception.errno, expected_errnos)

TestImaplib = test_imaplib.TestImaplib()
test_imap4_host_default_value()
