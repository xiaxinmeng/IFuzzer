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

def test_QUIT():
    SMTPDChannelTest.write_line(b'QUIT')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'221 Bye\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_QUIT()
