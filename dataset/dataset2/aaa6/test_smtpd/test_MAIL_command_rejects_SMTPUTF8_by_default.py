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

def test_MAIL_command_rejects_SMTPUTF8_by_default():
    SMTPDChannelTest.write_line(b'EHLO example')
    SMTPDChannelTest.write_line(b'MAIL from: <naive@example.com> BODY=8BITMIME SMTPUTF8')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last[0:1], b'5')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_MAIL_command_rejects_SMTPUTF8_by_default()
