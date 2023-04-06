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

def test_login():
    (client, _) = NewIMAPTestsMixin._setup(test_imaplib.SimpleIMAPHandler)
    (typ, data) = client.login('user', 'pass')
    NewIMAPTestsMixin.assertEqual(typ, 'OK')
    NewIMAPTestsMixin.assertEqual(data[0], b'LOGIN completed')
    NewIMAPTestsMixin.assertEqual(client.state, 'AUTH')

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_login()
