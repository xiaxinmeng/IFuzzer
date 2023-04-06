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

def test_valid_authentication_plain_text():

    class MyServer(test_imaplib.SimpleIMAPHandler):

        def cmd_AUTHENTICATE(NewIMAPTestsMixin, tag, args):
            NewIMAPTestsMixin._send_textline('+')
            NewIMAPTestsMixin.server.response = (yield)
            NewIMAPTestsMixin._send_tagged(tag, 'OK', 'FAKEAUTH successful')
    (client, server) = NewIMAPTestsMixin._setup(MyServer)
    (code, _) = client.authenticate('MYAUTH', lambda x: 'fake')
    NewIMAPTestsMixin.assertEqual(code, 'OK')
    NewIMAPTestsMixin.assertEqual(server.response, b'ZmFrZQ==\r\n')

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_valid_authentication_plain_text()
