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

def test_multiple_emails_with_extended_command_length():
    SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'ehlo example')
    fill_len = 512 + 26 + 10 - len('mail from:<@example>')
    for char in [b'a', b'b', b'c']:
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'MAIL from:<' + char * fill_len + b'a@example>')
        SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last[0:3], b'500')
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'MAIL from:<' + char * fill_len + b'@example>')
        SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last[0:3], b'250')
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'rcpt to:<hans@example.com>')
        SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last[0:3], b'250')
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'data')
        SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last[0:3], b'354')
        SMTPDChannelTestWithEnableSMTPUTF8True.write_line(b'test\r\n.')
        SMTPDChannelTestWithEnableSMTPUTF8True.assertEqual(SMTPDChannelTestWithEnableSMTPUTF8True.channel.socket.last[0:3], b'250')

SMTPDChannelTestWithEnableSMTPUTF8True = test_smtpd.SMTPDChannelTestWithEnableSMTPUTF8True()
SMTPDChannelTestWithEnableSMTPUTF8True.setUp()
test_multiple_emails_with_extended_command_length()
