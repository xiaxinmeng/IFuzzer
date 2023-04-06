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

@threading_helper.reap_threads
def test_search_disallows_charset_in_utf8_mode():
    with NewIMAPTestsMixin.reaped_pair(NewIMAPTestsMixin.UTF8Server) as (server, client):
        (typ, _) = client.authenticate('MYAUTH', lambda x: b'fake')
        NewIMAPTestsMixin.assertEqual(typ, 'OK')
        (typ, _) = client.enable('UTF8=ACCEPT')
        NewIMAPTestsMixin.assertEqual(typ, 'OK')
        NewIMAPTestsMixin.assertTrue(client.utf8_enabled)
        NewIMAPTestsMixin.assertRaises(imaplib.IMAP4.error, client.search, 'foo', 'bar')

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_search_disallows_charset_in_utf8_mode()
