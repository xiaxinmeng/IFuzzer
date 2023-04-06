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
def test_simple_with_statement():
    with NewIMAPTestsMixin.reaped_server(SimpleIMAPHandler) as server:
        with NewIMAPTestsMixin.imap_class(*server.server_address):
            pass

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_simple_with_statement()
