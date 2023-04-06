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

def test_nested_MAIL():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL from:eggs@example')
    SMTPDChannelTest.write_line(b'MAIL from:spam@example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'503 Error: nested MAIL command\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_nested_MAIL()
