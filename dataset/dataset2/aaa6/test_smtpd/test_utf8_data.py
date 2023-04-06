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

def test_utf8_data():
    SMTPDChannelWithDecodeDataFalse.write_line(b'EHLO example')
    SMTPDChannelWithDecodeDataFalse.write_line('MAIL From: naïve@examplé BODY=8BITMIME SMTPUTF8'.encode('utf-8'))
    SMTPDChannelWithDecodeDataFalse.assertEqual(SMTPDChannelWithDecodeDataFalse.channel.socket.last[0:3], b'250')
    SMTPDChannelWithDecodeDataFalse.write_line('RCPT To:späm@examplé'.encode('utf-8'))
    SMTPDChannelWithDecodeDataFalse.assertEqual(SMTPDChannelWithDecodeDataFalse.channel.socket.last[0:3], b'250')
    SMTPDChannelWithDecodeDataFalse.write_line(b'DATA')
    SMTPDChannelWithDecodeDataFalse.assertEqual(SMTPDChannelWithDecodeDataFalse.channel.socket.last[0:3], b'354')
    SMTPDChannelWithDecodeDataFalse.write_line(b'utf8 enriched text: \xc5\xbc\xc5\xba\xc4\x87')
    SMTPDChannelWithDecodeDataFalse.write_line(b'.')
    SMTPDChannelWithDecodeDataFalse.assertEqual(SMTPDChannelWithDecodeDataFalse.channel.received_data, b'utf8 enriched text: \xc5\xbc\xc5\xba\xc4\x87')

SMTPDChannelWithDecodeDataFalse = test_smtpd.SMTPDChannelWithDecodeDataFalse()
SMTPDChannelWithDecodeDataFalse.setUp()
test_utf8_data()
