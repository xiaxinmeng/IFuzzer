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

def test_data_dialog():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL From:eggs@example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelTest.write_line(b'RCPT To:spam@example')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelTest.write_line(b'DATA')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'354 End data with <CR><LF>.<CR><LF>\r\n')
    SMTPDChannelTest.write_line(b'data\r\nmore\r\n.')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.server.messages, [(('peer-address', 'peer-port'), 'eggs@example', ['spam@example'], 'data\nmore')])

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_data_dialog()
