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

def test_imaplib_timeout_functionality_test():

    class TimeoutHandler(test_imaplib.SimpleIMAPHandler):

        def handle(NewIMAPTestsMixin):
            time.sleep(1)
            test_imaplib.SimpleIMAPHandler.handle(NewIMAPTestsMixin)
    (_, server) = NewIMAPTestsMixin._setup(TimeoutHandler)
    addr = server.server_address[1]
    with NewIMAPTestsMixin.assertRaises(TimeoutError):
        client = NewIMAPTestsMixin.imap_class('localhost', addr, timeout=0.001)

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_imaplib_timeout_functionality_test()
