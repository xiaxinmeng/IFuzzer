import asyncore
import base64
import email.mime.text
from email.message import EmailMessage
from email.base64mime import body_encode as encode_base64
import email.utils
import hashlib
import hmac
import socket
import smtpd
import smtplib
import io
import re
import sys
import time
import select
import errno
import textwrap
import threading
import unittest
from test import support, mock_socket
from test.support import hashlib_helper
from test.support import socket_helper
from test.support import threading_helper
from unittest.mock import Mock
import test_smtplib

def test_debuglevel():
    mock_socket.reply_with(b'220 Hello world')
    client = GeneralTests.client()
    client.set_debuglevel(1)
    with support.captured_stderr() as stderr:
        client.connect(test_smtplib.HOST, GeneralTests.port)
    client.close()
    expected = re.compile('^connect:', re.MULTILINE)
    GeneralTests.assertRegex(stderr.getvalue(), expected)

GeneralTests = test_smtplib.GeneralTests()
GeneralTests.setUp()
test_debuglevel()
