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

def test_MAIL_allows_space_after_colon():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL from:   <foo@example.com>')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 OK\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_MAIL_allows_space_after_colon()
