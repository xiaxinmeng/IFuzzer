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

def test_logincapa():
    with socket_helper.transient_internet(RemoteIMAPTest.host):
        _server = RemoteIMAPTest.imap_class(RemoteIMAPTest.host, RemoteIMAPTest.port)
        RemoteIMAPTest.check_logincapa(_server)

RemoteIMAPTest = test_imaplib.RemoteIMAPTest()
test_logincapa()
