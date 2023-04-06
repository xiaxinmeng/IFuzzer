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

def test_MAIL_RCPT_unknown_parameters():
    SMTPDChannelTest.write_line(b'EHLO example')
    SMTPDChannelTest.write_line(b'MAIL FROM:<eggs@example> ham=green')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'555 MAIL FROM parameters not recognized or not implemented\r\n')
    SMTPDChannelTest.write_line(b'MAIL FROM:<eggs@example>')
    SMTPDChannelTest.write_line(b'RCPT TO:<eggs@example> ham=green')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'555 RCPT TO parameters not recognized or not implemented\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_MAIL_RCPT_unknown_parameters()
