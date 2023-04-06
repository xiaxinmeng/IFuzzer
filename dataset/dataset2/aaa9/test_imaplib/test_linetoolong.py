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

def test_linetoolong():

    class TooLongHandler(test_imaplib.SimpleIMAPHandler):

        def handle(NewIMAPTestsMixin):
            NewIMAPTestsMixin.wfile.write(b'* OK ' + imaplib._MAXLINE * b'x' + b'\r\n')
    with NewIMAPTestsMixin.reaped_server(TooLongHandler) as server:
        NewIMAPTestsMixin.assertRaises(imaplib.IMAP4.error, NewIMAPTestsMixin.imap_class, *server.server_address)

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_linetoolong()
