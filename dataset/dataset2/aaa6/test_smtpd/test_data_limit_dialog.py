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

def test_data_limit_dialog():
    SMTPDChannelWithDataSizeLimitTest.write_line(b'HELO example')
    SMTPDChannelWithDataSizeLimitTest.write_line(b'MAIL From:eggs@example')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelWithDataSizeLimitTest.write_line(b'RCPT To:spam@example')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelWithDataSizeLimitTest.write_line(b'DATA')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.channel.socket.last, b'354 End data with <CR><LF>.<CR><LF>\r\n')
    SMTPDChannelWithDataSizeLimitTest.write_line(b'data\r\nmore\r\n.')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.server.messages, [(('peer-address', 'peer-port'), 'eggs@example', ['spam@example'], 'data\nmore')])

SMTPDChannelWithDataSizeLimitTest = test_smtpd.SMTPDChannelWithDataSizeLimitTest()
test_data_limit_dialog()
