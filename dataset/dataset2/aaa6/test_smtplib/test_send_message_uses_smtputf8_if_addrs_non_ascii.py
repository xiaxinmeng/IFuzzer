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

def test_send_message_uses_smtputf8_if_addrs_non_ascii():
    msg = EmailMessage()
    msg['From'] = 'Páolo <főo@bar.com>'
    msg['To'] = 'Dinsdale'
    msg['Subject'] = 'Nudge nudge, wink, wink ὠ9'
    msg.set_content('oh là là, know what I mean, know what I mean?\n\n')
    expected = textwrap.dedent('            From: Páolo <főo@bar.com>\n            To: Dinsdale\n            Subject: Nudge nudge, wink, wink ὠ9\n            Content-Type: text/plain; charset="utf-8"\n            Content-Transfer-Encoding: 8bit\n            MIME-Version: 1.0\n\n            oh là là, know what I mean, know what I mean?\n            ')
    smtp = smtplib.SMTP(test_smtplib.HOST, SMTPUTF8SimTests.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    SMTPUTF8SimTests.addCleanup(smtp.close)
    SMTPUTF8SimTests.assertEqual(smtp.send_message(msg), {})
    SMTPUTF8SimTests.assertEqual(SMTPUTF8SimTests.serv.last_mailfrom, 'főo@bar.com')
    SMTPUTF8SimTests.assertEqual(SMTPUTF8SimTests.serv.last_rcpttos, ['Dinsdale'])
    SMTPUTF8SimTests.assertEqual(SMTPUTF8SimTests.serv.last_message.decode(), expected)
    SMTPUTF8SimTests.assertIn('BODY=8BITMIME', SMTPUTF8SimTests.serv.last_mail_options)
    SMTPUTF8SimTests.assertIn('SMTPUTF8', SMTPUTF8SimTests.serv.last_mail_options)
    SMTPUTF8SimTests.assertEqual(SMTPUTF8SimTests.serv.last_rcpt_options, [])

SMTPUTF8SimTests = test_smtplib.SMTPUTF8SimTests()
SMTPUTF8SimTests.setUp()
test_send_message_uses_smtputf8_if_addrs_non_ascii()
