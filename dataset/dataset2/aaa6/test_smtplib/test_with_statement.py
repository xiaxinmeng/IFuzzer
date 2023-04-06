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

def test_with_statement():
    with smtplib.SMTP(test_smtplib.HOST, SMTPSimTests.port) as smtp:
        (code, message) = smtp.noop()
        SMTPSimTests.assertEqual(code, 250)
    SMTPSimTests.assertRaises(smtplib.SMTPServerDisconnected, smtp.send, b'foo')
    with smtplib.SMTP(test_smtplib.HOST, SMTPSimTests.port) as smtp:
        smtp.close()
    SMTPSimTests.assertRaises(smtplib.SMTPServerDisconnected, smtp.send, b'foo')

SMTPSimTests = test_smtplib.SMTPSimTests()
SMTPSimTests.setUp()
test_with_statement()
