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

def test_HELO_parameter_rejected_when_extensions_not_enabled():
    SMTPDChannelTest.extended_smtp = False
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL from:<foo@example.com> SIZE=1234')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'501 Syntax: MAIL FROM: <address>\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_HELO_parameter_rejected_when_extensions_not_enabled()
