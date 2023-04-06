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

def test_quit_resets_greeting():
    smtp = smtplib.SMTP(test_smtplib.HOST, SMTPSimTests.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    (code, message) = smtp.ehlo()
    SMTPSimTests.assertEqual(code, 250)
    SMTPSimTests.assertIn('size', smtp.esmtp_features)
    smtp.quit()
    SMTPSimTests.assertNotIn('size', smtp.esmtp_features)
    smtp.connect(test_smtplib.HOST, SMTPSimTests.port)
    SMTPSimTests.assertNotIn('size', smtp.esmtp_features)
    smtp.ehlo_or_helo_if_needed()
    SMTPSimTests.assertIn('size', smtp.esmtp_features)
    smtp.quit()

SMTPSimTests = test_smtplib.SMTPSimTests()
SMTPSimTests.setUp()
test_quit_resets_greeting()
