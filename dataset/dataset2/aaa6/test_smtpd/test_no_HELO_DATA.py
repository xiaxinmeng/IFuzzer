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

def test_no_HELO_DATA():
    SMTPDChannelTest.write_line(b'DATA spam')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'503 Error: send HELO first\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_no_HELO_DATA()
