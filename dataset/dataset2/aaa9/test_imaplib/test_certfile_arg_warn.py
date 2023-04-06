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

@cpython_only
def test_certfile_arg_warn():
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        with mock.patch.object(NewIMAPSSLTests.imap_class, 'open'):
            with mock.patch.object(NewIMAPSSLTests.imap_class, '_connect'):
                NewIMAPSSLTests.imap_class('localhost', 143, certfile=test_imaplib.CERTFILE)

NewIMAPSSLTests = test_imaplib.NewIMAPSSLTests()
test_certfile_arg_warn()
