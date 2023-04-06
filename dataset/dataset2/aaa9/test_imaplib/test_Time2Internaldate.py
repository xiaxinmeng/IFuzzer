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

@run_with_locale('LC_ALL', 'de_DE', 'fr_FR')
@run_with_tz('STD-1DST,M3.2.0,M11.1.0')
def test_Time2Internaldate():
    expected = '"18-May-2033 05:33:20 +0200"'
    for t in TestImaplib.timevalues():
        internal = imaplib.Time2Internaldate(t)
        TestImaplib.assertEqual(internal, expected)

TestImaplib = test_imaplib.TestImaplib()
test_Time2Internaldate()
