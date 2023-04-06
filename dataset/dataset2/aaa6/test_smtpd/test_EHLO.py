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

def test_EHLO():
    SMTPDChannelTest.write_line(b'EHLO example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 HELP\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_EHLO()
