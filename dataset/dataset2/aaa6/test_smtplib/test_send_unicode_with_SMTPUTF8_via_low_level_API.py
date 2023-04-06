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

def test_send_unicode_with_SMTPUTF8_via_low_level_API():
    m = '¡a test message containing unicode!'.encode('utf-8')
    smtp = smtplib.SMTP(test_smtplib.HOST, SMTPUTF8SimTests.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    SMTPUTF8SimTests.addCleanup(smtp.close)
    smtp.ehlo()
    SMTPUTF8SimTests.assertEqual(smtp.mail('Jő', options=['BODY=8BITMIME', 'SMTPUTF8']), (250, b'OK'))
    SMTPUTF8SimTests.assertEqual(smtp.rcpt('János'), (250, b'OK'))
    SMTPUTF8SimTests.assertEqual(smtp.data(m), (250, b'OK'))
    SMTPUTF8SimTests.assertEqual(SMTPUTF8SimTests.serv.last_mailfrom, 'Jő')
    SMTPUTF8SimTests.assertEqual(SMTPUTF8SimTests.serv.last_rcpttos, ['János'])
    SMTPUTF8SimTests.assertEqual(SMTPUTF8SimTests.serv.last_message, m)
    SMTPUTF8SimTests.assertIn('BODY=8BITMIME', SMTPUTF8SimTests.serv.last_mail_options)
    SMTPUTF8SimTests.assertIn('SMTPUTF8', SMTPUTF8SimTests.serv.last_mail_options)
    SMTPUTF8SimTests.assertEqual(SMTPUTF8SimTests.serv.last_rcpt_options, [])

SMTPUTF8SimTests = test_smtplib.SMTPUTF8SimTests()
SMTPUTF8SimTests.setUp()
test_send_unicode_with_SMTPUTF8_via_low_level_API()
