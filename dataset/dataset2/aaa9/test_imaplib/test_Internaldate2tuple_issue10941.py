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

@run_with_tz('MST+07MDT,M4.1.0,M10.5.0')
def test_Internaldate2tuple_issue10941():
    TestImaplib.assertNotEqual(imaplib.Internaldate2tuple(b'25 (INTERNALDATE "02-Apr-2000 02:30:00 +0000")'), imaplib.Internaldate2tuple(b'25 (INTERNALDATE "02-Apr-2000 03:30:00 +0000")'))

TestImaplib = test_imaplib.TestImaplib()
test_Internaldate2tuple_issue10941()
