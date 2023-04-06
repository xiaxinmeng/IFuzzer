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

@hashlib_helper.requires_hashdigest('md5')
def test_login_cram_md5_bytes():

    class AuthHandler(test_imaplib.SimpleIMAPHandler):
        capabilities = 'LOGINDISABLED AUTH=CRAM-MD5'

        def cmd_AUTHENTICATE(NewIMAPTestsMixin, tag, args):
            NewIMAPTestsMixin._send_textline('+ PDE4OTYuNjk3MTcwOTUyQHBvc3RvZmZpY2UucmVzdG9uLm1jaS5uZXQ=')
            r = (yield)
            if r == b'dGltIGYxY2E2YmU0NjRiOWVmYTFjY2E2ZmZkNmNmMmQ5ZjMy\r\n':
                NewIMAPTestsMixin._send_tagged(tag, 'OK', 'CRAM-MD5 successful')
            else:
                NewIMAPTestsMixin._send_tagged(tag, 'NO', 'No access')
    (client, _) = NewIMAPTestsMixin._setup(AuthHandler)
    NewIMAPTestsMixin.assertTrue('AUTH=CRAM-MD5' in client.capabilities)
    (ret, _) = client.login_cram_md5('tim', b'tanstaaftanstaaf')
    NewIMAPTestsMixin.assertEqual(ret, 'OK')

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_login_cram_md5_bytes()
