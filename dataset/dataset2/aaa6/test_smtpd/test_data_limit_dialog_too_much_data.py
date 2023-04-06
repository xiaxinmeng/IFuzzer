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

def test_data_limit_dialog_too_much_data():
    SMTPDChannelWithDataSizeLimitTest.write_line(b'HELO example')
    SMTPDChannelWithDataSizeLimitTest.write_line(b'MAIL From:eggs@example')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelWithDataSizeLimitTest.write_line(b'RCPT To:spam@example')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.channel.socket.last, b'250 OK\r\n')
    SMTPDChannelWithDataSizeLimitTest.write_line(b'DATA')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.channel.socket.last, b'354 End data with <CR><LF>.<CR><LF>\r\n')
    SMTPDChannelWithDataSizeLimitTest.write_line(b'This message is longer than 32 bytes\r\n.')
    SMTPDChannelWithDataSizeLimitTest.assertEqual(SMTPDChannelWithDataSizeLimitTest.channel.socket.last, b'552 Error: Too much mail data\r\n')

SMTPDChannelWithDataSizeLimitTest = test_smtpd.SMTPDChannelWithDataSizeLimitTest()
SMTPDChannelWithDataSizeLimitTest.setUp()
test_data_limit_dialog_too_much_data()
