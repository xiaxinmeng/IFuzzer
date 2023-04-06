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

def test_bad_state():
    SMTPDChannelTest.channel.smtp_state = 'BAD STATE'
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'451 Internal confusion\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_bad_state()
