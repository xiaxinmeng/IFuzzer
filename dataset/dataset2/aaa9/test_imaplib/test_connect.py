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
def test_connect():
    with ThreadedNetworkedTests.reaped_server(test_imaplib.SimpleIMAPHandler) as server:
        client = ThreadedNetworkedTests.imap_class(*server.server_address)
        client.shutdown()

ThreadedNetworkedTests = test_imaplib.ThreadedNetworkedTests()
test_connect()
