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

def test_send_unicode_without_SMTPUTF8():
    smtp = smtplib.SMTP(test_smtplib.HOST, SMTPSimTests.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    SMTPSimTests.addCleanup(smtp.close)
    SMTPSimTests.assertRaises(UnicodeEncodeError, smtp.sendmail, 'Alice', 'Böb', '')
    SMTPSimTests.assertRaises(UnicodeEncodeError, smtp.mail, 'Älice')

SMTPSimTests = test_smtplib.SMTPSimTests()
SMTPSimTests.setUp()
test_send_unicode_without_SMTPUTF8()
