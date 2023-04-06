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

def test_HELO():
    name = smtpd.socket.getfqdn()
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, '250 {}\r\n'.format(name).encode('ascii'))

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_HELO()
