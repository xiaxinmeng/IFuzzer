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

def test_EOF_without_complete_welcome_message():

    class EOFHandler(socketserver.StreamRequestHandler):

        def handle(NewIMAPTestsMixin):
            NewIMAPTestsMixin.wfile.write(b'* OK')
    (_, server) = NewIMAPTestsMixin._setup(EOFHandler, connect=False)
    NewIMAPTestsMixin.assertRaises(imaplib.IMAP4.abort, NewIMAPTestsMixin.imap_class, *server.server_address)

NewIMAPTestsMixin = test_imaplib.NewIMAPTestsMixin()
test_EOF_without_complete_welcome_message()
