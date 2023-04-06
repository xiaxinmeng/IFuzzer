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

def test_MAIL_quoted_localpart():
    SMTPDChannelTest.write_line(b'EHLO example')
    SMTPDChannelTest.write_line(b'MAIL from: <"Fred Blogs"@example.com>')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.mailfrom, '"Fred Blogs"@example.com')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_MAIL_quoted_localpart()
