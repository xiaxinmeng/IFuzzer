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

def test_RSET():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL From:eggs@example')
    SMTPDChannelTest.write_line(b'RCPT To:spam@example')
    SMTPDChannelTest.write_line(b'RSET')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelTest.write_line(b'MAIL From:foo@example')
    SMTPDChannelTest.write_line(b'RCPT To:eggs@example')
    SMTPDChannelTest.write_line(b'DATA')
    SMTPDChannelTest.write_line(b'data\r\n.')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.server.messages, [(('peer-address', 'peer-port'), 'foo@example', ['eggs@example'], 'data')])

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_RSET()
