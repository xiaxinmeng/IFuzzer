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

def test_logout():
    with socket_helper.transient_internet(NewIMAPTestsMixin.host):
        _server = NewIMAPTestsMixin.imap_class(NewIMAPTestsMixin.host, NewIMAPTestsMixin.port)
        rs = _server.logout()
        NewIMAPTestsMixin.assertEqual(rs[0], 'BYE', rs)

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_logout()
