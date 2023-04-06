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

def test_command_too_long():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL from: ' + b'a' * SMTPDChannelTest.channel.command_size_limit + b'@example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'500 Error: line too long\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_command_too_long()
