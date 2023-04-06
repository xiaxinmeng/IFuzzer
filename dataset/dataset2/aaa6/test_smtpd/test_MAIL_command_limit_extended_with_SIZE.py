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

def test_MAIL_command_limit_extended_with_SIZE():
    SMTPDChannelTest.write_line(b'EHLO example')
    fill_len = SMTPDChannelTest.channel.command_size_limit - len('MAIL from:<@example>')
    SMTPDChannelTest.write_line(b'MAIL from:<' + b'a' * fill_len + b'@example> SIZE=1234')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelTest.write_line(b'MAIL from:<' + b'a' * (fill_len + 26) + b'@example> SIZE=1234')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'500 Error: line too long\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_MAIL_command_limit_extended_with_SIZE()
