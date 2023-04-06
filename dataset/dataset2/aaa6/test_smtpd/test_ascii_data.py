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

def test_ascii_data():
    SMTPDChannelWithDecodeDataFalse.write_line(b'HELO example')
    SMTPDChannelWithDecodeDataFalse.write_line(b'MAIL From:eggs@example')
    SMTPDChannelWithDecodeDataFalse.write_line(b'RCPT To:spam@example')
    SMTPDChannelWithDecodeDataFalse.write_line(b'DATA')
    SMTPDChannelWithDecodeDataFalse.write_line(b'plain ascii text')
    SMTPDChannelWithDecodeDataFalse.write_line(b'.')
    SMTPDChannelWithDecodeDataFalse.assertEqual(SMTPDChannelWithDecodeDataFalse.channel.received_data, 'plain ascii text')

SMTPDChannelWithDecodeDataFalse = test_smtpd.SMTPDChannelWithDecodeDataFalse()
SMTPDChannelWithDecodeDataFalse.setUp()
test_ascii_data()
