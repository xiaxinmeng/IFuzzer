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

def test_manual_status():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL From:eggs@example')
    SMTPDChannelTest.write_line(b'RCPT To:spam@example')
    SMTPDChannelTest.write_line(b'DATA')
    SMTPDChannelTest.write_line(b'return status\r\n.')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.socket.last, b'250 Okish\r\n')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_manual_status()
