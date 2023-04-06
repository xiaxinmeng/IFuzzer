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
def test_issue5949():

    class EOFHandler(socketserver.StreamRequestHandler):

        def handle(ThreadedNetworkedTests):
            ThreadedNetworkedTests.wfile.write(b'* OK')
    with ThreadedNetworkedTests.reaped_server(EOFHandler) as server:
        ThreadedNetworkedTests.assertRaises(imaplib.IMAP4.abort, ThreadedNetworkedTests.imap_class, *server.server_address)

ThreadedNetworkedTests = test_imaplib.ThreadedNetworkedTests()
test_issue5949()
