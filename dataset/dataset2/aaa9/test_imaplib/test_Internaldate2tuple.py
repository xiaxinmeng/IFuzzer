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

def test_Internaldate2tuple():
    t0 = calendar.timegm((2000, 1, 1, 0, 0, 0, -1, -1, -1))
    tt = imaplib.Internaldate2tuple(b'25 (INTERNALDATE "01-Jan-2000 00:00:00 +0000")')
    TestImaplib.assertEqual(time.mktime(tt), t0)
    tt = imaplib.Internaldate2tuple(b'25 (INTERNALDATE "01-Jan-2000 11:30:00 +1130")')
    TestImaplib.assertEqual(time.mktime(tt), t0)
    tt = imaplib.Internaldate2tuple(b'25 (INTERNALDATE "31-Dec-1999 12:30:00 -1130")')
    TestImaplib.assertEqual(time.mktime(tt), t0)

TestImaplib = test_imaplib.TestImaplib()
test_Internaldate2tuple()
