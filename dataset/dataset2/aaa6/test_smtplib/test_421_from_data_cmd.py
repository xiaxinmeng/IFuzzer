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

def test_421_from_data_cmd():

    class MySimSMTPChannel(test_smtplib.SimSMTPChannel):

        def found_terminator(SMTPSimTests):
            if SMTPSimTests.smtp_state == SMTPSimTests.DATA:
                SMTPSimTests.push('421 closing')
            else:
                super().found_terminator()
    SMTPSimTests.serv.channel_class = MySimSMTPChannel
    smtp = smtplib.SMTP(test_smtplib.HOST, SMTPSimTests.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    smtp.noop()
    with SMTPSimTests.assertRaises(smtplib.SMTPDataError):
        smtp.sendmail('John@foo.org', ['Sally@foo.org'], 'test message')
    SMTPSimTests.assertIsNone(smtp.sock)
    SMTPSimTests.assertEqual(SMTPSimTests.serv._SMTPchannel.rcpt_count, 0)

SMTPSimTests = test_smtplib.SMTPSimTests()
SMTPSimTests.setUp()
test_421_from_data_cmd()
