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

def test_EXPN_not_implemented():
    SMTPDChannelTest.write_line(b'EXPN')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'502 EXPN not implemented\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_EXPN_not_implemented()
