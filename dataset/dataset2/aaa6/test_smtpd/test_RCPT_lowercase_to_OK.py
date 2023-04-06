import unittest
import textwrap
from test import support, mock_socket
from test.support import socket_helper
from test.support import warnings_helper
import socket
import io
import smtpd
import asyncore
import test_smtpd

def test_RCPT_lowercase_to_OK():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL From: eggs@example')
    SMTPDChannelTest.write_line(b'RCPT to: <eggs@example>')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 OK\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_RCPT_lowercase_to_OK()
