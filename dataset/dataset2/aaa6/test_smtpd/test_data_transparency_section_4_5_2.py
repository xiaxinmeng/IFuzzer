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

def test_data_transparency_section_4_5_2():
    SMTPDChannelTest.write_line(b'HELO example')
    SMTPDChannelTest.write_line(b'MAIL From:eggs@example')
    SMTPDChannelTest.write_line(b'RCPT To:spam@example')
    SMTPDChannelTest.write_line(b'DATA')
    SMTPDChannelTest.write_line(b'..\r\n.\r\n')
    SMTPDChannelTest.assertEqual(SMTPDChannelTest.channel.received_data, '.')

SMTPDChannelTest = test_smtpd.SMTPDChannelTest()
SMTPDChannelTest.setUp()
test_data_transparency_section_4_5_2()
