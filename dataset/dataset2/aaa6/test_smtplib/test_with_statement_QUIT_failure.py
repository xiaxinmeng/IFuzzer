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

def test_with_statement_QUIT_failure():
    with SMTPSimTests.assertRaises(smtplib.SMTPResponseException) as error:
        with smtplib.SMTP(test_smtplib.HOST, SMTPSimTests.port) as smtp:
            smtp.noop()
            SMTPSimTests.serv._SMTPchannel.quit_response = '421 QUIT FAILED'
    SMTPSimTests.assertEqual(error.exception.smtp_code, 421)
    SMTPSimTests.assertEqual(error.exception.smtp_error, b'QUIT FAILED')

SMTPSimTests = test_smtplib.SMTPSimTests()
SMTPSimTests.setUp()
test_with_statement_QUIT_failure()
