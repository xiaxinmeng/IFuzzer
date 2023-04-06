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

def test_VRFY():
    SMTPDChannelTest.write_line(b'VRFY eggs@example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'252 Cannot VRFY user, but will accept message and attempt ' + b'delivery\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_VRFY()
