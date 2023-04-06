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

def test_need_MAIL():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'RCPT to:spam@example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'503 Error: need MAIL command\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_need_MAIL()
