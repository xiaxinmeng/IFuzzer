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

def test_HELP():
    SMTPDChannelTest.write_line(b'HELP')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 Supported commands: EHLO HELO MAIL RCPT ' + b'DATA RSET NOOP QUIT VRFY\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_HELP()
