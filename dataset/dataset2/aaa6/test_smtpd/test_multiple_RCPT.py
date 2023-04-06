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

def test_multiple_RCPT():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL From:eggs@example')
    SMTPDChannelTest.write_line(b'RCPT To:spam@example')
    SMTPDChannelTest.write_line(b'RCPT To:ham@example')
    SMTPDChannelTest.write_line(b'DATA')
    SMTPDChannelTest.write_line(b'data\r\n.')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.server.messages, [(('peer-address', 'peer-port'), 'eggs@example', ['spam@example', 'ham@example'], 'data')])

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_multiple_RCPT()
