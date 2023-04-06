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

def test_ssl_context_certfile_exclusive():
    with socket_helper.transient_internet(RemoteIMAP_SSLTest.host):
        RemoteIMAP_SSLTest.assertRaises(ValueError, RemoteIMAP_SSLTest.imap_class, RemoteIMAP_SSLTest.host, RemoteIMAP_SSLTest.port, certfile=test_imaplib.CERTFILE, ssl_context=RemoteIMAP_SSLTest.create_ssl_context())

RemoteIMAP_SSLTest = test_imaplib.RemoteIMAP_SSLTest()
test_ssl_context_certfile_exclusive()
